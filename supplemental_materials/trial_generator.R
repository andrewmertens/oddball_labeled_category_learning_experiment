library(dplyr)
library(stringr)
library(openxlsx)

##############
#create transition matrix representing the valid transitions between orientations
#1's represent valid transitions, 0's are invalid transitions
#ex: the 1 at [1,3] means that transitions from orientation 3 to orientation 1 are valid
#this matrix is symmetrical so [3,1] is also valid
transitions_oddball_high <-       c(0,1,1,1,0,0,1,1,
                                    1,0,1,1,0,0,1,1,
                                    1,1,0,1,1,1,0,0,
                                    1,1,1,0,1,1,0,0,
                                    0,0,1,1,0,0,0,0,
                                    0,0,1,1,0,0,0,0,
                                    1,1,0,0,0,0,0,0,
                                    1,1,0,0,0,0,0,0)

transMat_oddball_high <- matrix(data = transitions_oddball_high, nrow=8)

transitions_oddball_low <-         c(0,0,0,0,0,0,1,1,
                                     0,0,0,0,0,0,1,1,
                                     0,0,0,0,1,1,0,0,
                                     0,0,0,0,1,1,0,0,
                                     0,0,1,1,0,1,1,1,
                                     0,0,1,1,1,0,1,1,
                                     1,1,0,0,1,1,0,1,
                                     1,1,0,0,1,1,1,0)

transMat_oddball_low <- matrix(data = transitions_oddball_low, nrow=8)


#creates a sequence based on legal transitions given a transition matrix
###KNOWN ISSUES: VERY occasionally includes steps of 0 (i.e., same orientation shown twice in a row) 
#- this occurs when a bookend is chosen that happens to match the second to last ori in a block
#sequenceR(transMat_oddball_low, oddball = 'low', blocks = 100, seed=1) - end of block 27 in this sequence, for example
sequenceR <- function(transition_matrix, blocks=1, oddball, seed=NULL, initialization=NULL) {
  if (!is.null(seed)) {
    set.seed(seed)
  }
  
  if (is.null(initialization)) {
    first_ori <- sample(1:8, 1)
  } else first_ori <- initialization #initialization orientation
  
  if (oddball=='high') {
    stand_oris <- 1:4
    dev_oris <- 5:8
  } else if (oddball == 'low'){
    stand_oris <- 5:8
    dev_oris <- 1:4
  }
  
  steps <- NA
  full_seq <- vector("numeric")
  
  for (b in 1:blocks) {
    block_seq <- first_ori
    tm <- transition_matrix
    curr_item_idx <- 1
    bookend_ori <- NA
    
    while (length(block_seq) < 16) {
      curr_ori <- block_seq[curr_item_idx]
      ori_options <- which(tm[,curr_ori]==T) #returns list of viable next orientations given available legal transitions from current ori
      
       if (length(block_seq)==15 & !is.na(bookend_ori)) {
        next_ori <- bookend_ori
      } else if (length(ori_options)==0) {
        #^these oddball transition matrices have the issue that they cannot loop between each transition seamlessly
        #^this first checks to see if there are no legal transition options
        #if there are none, we choose an orientation in the 3-step range that still has moves
        three_step_range <- seq(curr_ori-3,curr_ori+3)
        three_step_range <- case_match(three_step_range, -2 ~ 6, -1 ~ 7, 0 ~ 8, 9 ~ 1, 10 ~ 2, 11 ~ 3, .default = three_step_range)
        
        if (is.na(bookend_ori)) {
          trackjump_ori_opt <- three_step_range[three_step_range != curr_ori & three_step_range %in% stand_oris]
        } else trackjump_ori_opt <- three_step_range[three_step_range != curr_ori & three_step_range %in% stand_oris & three_step_range != bookend_ori]
        #the rule for choosing which orientation to 'jump' to got very complicated:
        if (length(trackjump_ori_opt)>1) {
          tm_col_sums <- colSums(tm[,trackjump_ori_opt])
          max_moves <- suppressWarnings(max(tm_col_sums[tm_col_sums>0 & tm_col_sums %% 2 == 1])) #if there are any orientations with an odd number of moves remaining, take the highest
          
          if (max_moves==-Inf) max_moves <- max(tm_col_sums[tm_col_sums>0]) # if not^, take the highest
          max_move_oris <- which(colSums(tm[,trackjump_ori_opt])==max_moves)
          trackjump_ori <- trackjump_ori_opt[max_move_oris][sample(1:length(trackjump_ori_opt[max_move_oris]), 1)] #if there is a tie, select one at random
          next_ori <- trackjump_ori
        } else next_ori <- trackjump_ori_opt
          
        
      } else next_ori <- ori_options[sample(1:length(ori_options), 1)] #randomly select next ori given legal transitions
      #^(sample syntax allows it to select the only choice if there is only one valid transition)
      
       
      
      step_size <- abs(next_ori-curr_ori)
      #because orientation stimuli are distributed circularly, a transition from,
      #say, 1 to 8 could be conceived of as a 7 step difference, or a 1 step
      #difference depending on which direction you go; this converts step size 
      #differences to reflect the more sensible, shorter distance:
      step_size <- case_match(step_size,7~1,6~2,5~3, .default = step_size) 
      
      steps <- c(steps, step_size)
      
      tm[next_ori,curr_ori] <- 0
      tm[curr_ori,next_ori] <- 0
      
      #1. look at first transition,
      #2. select another transition to remove from same standard-standard (e.g., high-high) set or deviant-standard (e.g., high-low) set
      #3. save the orientation from the removed set that is not the current orientation, to place as final ori in sequence
      if (length(block_seq)==1 & next_ori %in% stand_oris) {
        if (curr_ori %in% stand_oris) {
          subtm <- tm[stand_oris, stand_oris]
          curr_ori_indx <- which(stand_oris==curr_ori)
          curr_ori_trans <- stand_oris[which(subtm[,curr_ori_indx]==T)]
          bookend_options <- stand_oris[stand_oris %in% curr_ori_trans]
          bookend_ori <- bookend_options[sample(1:length(bookend_options), 1)]
        } else {
          subtm <- tm[stand_oris,dev_oris] #symmetrical, but let's call the rows the standards and the columns the deviants
          if (curr_ori %in% dev_oris){
            curr_ori_indx <- which(dev_oris==curr_ori)
            curr_ori_trans <- stand_oris[which(subtm[,curr_ori_indx]==T)]
            bookend_ori <- stand_oris[stand_oris %in% curr_ori_trans]
          } else if (curr_ori %in% stand_oris) {
            curr_ori_indx <- which(stand_oris==curr_ori)
            curr_ori_trans <- dev_oris[which(subtm[curr_ori_indx,]==T)]
            bookend_ori <- dev_oris[dev_oris %in% curr_ori_trans]
          }
        }
        tm[bookend_ori,curr_ori] <- 0
        tm[curr_ori,bookend_ori] <- 0
      }
      
      block_seq <- c(block_seq, next_ori)
      curr_item_idx <- length(block_seq)
      
    }
    full_seq <- c(full_seq, block_seq)
    last_block_ori <- tail(block_seq, 1)
    next_first_ori <- sample(c((last_block_ori+3),(last_block_ori-3)),1) #select the next block's initialization; have it represent a 3-step transition as those are underrepresented
    first_ori <- case_match(next_first_ori, -2 ~ 6, -1 ~ 7, 0 ~ 8, 9 ~ 1, 10 ~ 2, 11 ~ 3, .default = next_first_ori)
    if (b<blocks) steps <- c(steps, 3)
    
    }
  return(cbind(full_seq,steps))
}

#to check to see if distributions of orientations are good, and identify iterations where they are not
# bad_seed <- NA
# s <- 1
# while (is.na(bad_seed)) {
#   ori_dist <- table(sequenceR(transMat_oddball_low, oddball = 'low', blocks = 2, initialization = 6, seed=s)[,1])
#   if (all(ori_dist[1:4]==2) & all(ori_dist[5:8]==6)) {
#     s <- s+1
#   } else bad_seed <- s
# }


seq_to_cond <- function(seq_set, seed, oddball, #oddball: if low orientations are deviant, set oddball equal to 'low'
                        or1, or2, or3, or4, or5, or6, or7, or8,
                        sf1, sf2, sf3, sf4, sf5, sf6, sf7, sf8) {
  set.seed(seed)
  
  if (oddball=='high') {
    stand_oris <- 1:4
    dev_oris <- 5:8
  } else if (oddball == 'low'){
    stand_oris <- 5:8
    dev_oris <- 1:4
  }
  
  #puts sequences (created by 'sequenceR' function) in a single column of a dataframe:
  #seq_len <- ((str_length(seq_set[1])-1)/2)
  seq_mat_names <- c("learn_ori_lab", "learn_ori_steps", "learn_block", "learn_ori_val",
                     "learn_stim_type", "learn_trial_type", "learn_freq_lab", 
                     "learn_pos_lab", "learn_freq_val", "learn_explor_pos_LR",
                     "learn_explor_pos_UD", "learn_legal_keys", "learn_correct_key",
                     "learn_ontrig", "learn_offtrig")
  seq_mat <- data.frame(matrix(ncol=length(seq_mat_names),nrow = nrow(seq_set)))
  names(seq_mat) <- seq_mat_names
  
  seq_mat[,"learn_ori_lab"] <- seq_set[,1]
  seq_mat[,"learn_ori_steps"] <- seq_set[,2]
  seq_mat[,"learn_block"] <- rep(1:(nrow(seq_set)/16), each = 16)
  
  #converts orientation labels to orientation values:
  seq_mat$learn_ori_val <- case_match(seq_mat$learn_ori_lab,
                                  1 ~ or1,
                                  2 ~ or2,
                                  3 ~ or3,
                                  4 ~ or4,
                                  5 ~ or5,
                                  6 ~ or6,
                                  7 ~ or7,
                                  8 ~ or8)
  #uses orientation labels to create labels for trial types (friendly vs hostile)
  ##changed for this experiment so that hostile = vertical; early study showed that this association facilitated learning
  seq_mat$learn_stim_type <- case_match(seq_mat$learn_ori_lab,
                                     1 ~ "hostile",
                                     2 ~ "hostile",
                                     3 ~ "hostile",
                                     4 ~ "hostile",
                                     5 ~ "friendly",
                                     6 ~ "friendly",
                                     7 ~ "friendly",
                                     8 ~ "friendly")
  #labels deviant and standard trials
   seq_mat$learn_trial_type <- case_when(seq_mat$learn_ori_lab %in% stand_oris ~ "standard",
                                                 seq_mat$learn_ori_lab %in% dev_oris ~ "deviant")
   
  #GENERATES SEQUENCE OF FREQUENCIES THAT CREATES A RELATIVELY EVEN DISTRIBUTION OF EXPOSURES TO EACH UNIQUE STIMULI
  stim_mat <- matrix(0, nrow = 8, ncol = 8) #rows = ori, cols = freq
  for (trial in 1:nrow(seq_mat)) {
    ori <- seq_mat$learn_ori_lab[trial] 
    min_freq_count <- min(stim_mat[ori,]) #returns the minimum number of times any frequency has been paired with that orientation
    min_freqs <- which(stim_mat[ori,] == min_freq_count) #returns a list of frequencies that are at that minimum^
    if (length(min_freqs)>1){ #if only one frequency meets that condition, ELSE sets the frequency to that
      min_col_tots <- min(colSums(stim_mat[,min_freqs])) #if more than one, looks at number of times each frequency in the list^ have been used overall and chooses (one of) the least
      min_freqs_per_col_indx <- colSums(stim_mat[,min_freqs]) == min_col_tots
      min_freqs_per_col <- min_freqs[min_freqs_per_col_indx]
      next_freq <- min_freqs_per_col[sample(1:length(min_freqs_per_col), 1)]
    } else next_freq <- min_freqs
     #chooses one^ at random
    stim_mat[ori,next_freq] <- stim_mat[ori,next_freq]+1
    
    #seq_mat$learn_freq_lab[trial] <- next_freq
    seq_mat$learn_freq_lab[trial] <- next_freq
  }
   
  #generates random sequence of explorer position labels (1-4)
  tot_blocks <- max(seq_mat$learn_block, na.rm=T)
  explor_seeds <- sample(1:1000, tot_blocks, replace=F) #Note that this command itself is seeded, allowing multiple unique sequences to be generated in a consistent way
  for (i in 1:tot_blocks) {
    set.seed(explor_seeds[i])
    pos_seq <- sample(rep(1:4, 4), replace = F)
    seq_mat[which(seq_mat$learn_block==i),"learn_pos_lab"] <- pos_seq
  }
  #converts frequency labels to frequency values
  seq_mat$learn_freq_val <- recode(seq_mat$learn_freq_lab,
                                    "1" = sf1,
                                    "2" = sf2,
                                    "3" = sf3,
                                    "4" = sf4,
                                    "5" = sf5,
                                    "6" = sf6,
                                    "7" = sf7,
                                    "8" = sf8)
  #converts position labels to more intuitive values
  seq_mat$learn_pos_lab <- case_match(seq_mat$learn_pos_lab,
                                  1 ~ "u",
                                  2 ~ "d",
                                  3 ~ "l",
                                  4 ~ "r")
  #converts position labels to left-right values
  seq_mat$learn_explor_pos_LR <- recode(seq_mat$learn_pos_lab,
                                        "u" = 0,
                                        "d" = 0,
                                        "l" = -.2,
                                        "r" = .2)
  #converts position labels to up-down values
  seq_mat$learn_explor_pos_UD <- recode(seq_mat$learn_pos_lab,
                                        "u" = .25,
                                        "d" = -.25,
                                        "l" = 0,
                                        "r" = 0)
  #creates list of legal key presses based on position label
  seq_mat$learn_legal_keys <- recode(seq_mat$learn_pos_lab,
                                     "u" = "['up','down']",
                                     "d" = "['up','down']",
                                     "l" = "['left','right']",
                                     "r" = "['left','right']")
  #generates correct key presses based on trial type and position label
  seq_mat$learn_correct_key <- case_when(
    seq_mat$learn_stim_type == "friendly" & seq_mat$learn_pos_lab == "u" ~ "down",
    seq_mat$learn_stim_type == "friendly" & seq_mat$learn_pos_lab == "d" ~ "up",
    seq_mat$learn_stim_type == "friendly" & seq_mat$learn_pos_lab == "l" ~ "right",
    seq_mat$learn_stim_type == "friendly" & seq_mat$learn_pos_lab == "r" ~ "left",
    seq_mat$learn_stim_type == "hostile" & seq_mat$learn_pos_lab == "u" ~ "up",
    seq_mat$learn_stim_type == "hostile" & seq_mat$learn_pos_lab == "d" ~ "down",
    seq_mat$learn_stim_type == "hostile" & seq_mat$learn_pos_lab == "l" ~ "left",
    seq_mat$learn_stim_type == "hostile" & seq_mat$learn_pos_lab == "r" ~ "right")
  
  seq_mat$learn_ontrig = case_when(
    #block 1
    seq_mat$learn_block == 1 & seq_mat$learn_stim_type == "hostile" & seq_mat$learn_trial_type == "standard" & is.na(seq_mat$learn_ori_steps) ~ 27,
    seq_mat$learn_block == 1 & seq_mat$learn_stim_type == "hostile" & seq_mat$learn_trial_type == "deviant" & is.na(seq_mat$learn_ori_steps) ~ 28,
    seq_mat$learn_block == 1 & seq_mat$learn_stim_type == "friendly" & seq_mat$learn_trial_type == "standard" & is.na(seq_mat$learn_ori_steps) ~ 29,
    seq_mat$learn_block == 1 & seq_mat$learn_stim_type == "friendly" & seq_mat$learn_trial_type == "deviant" & is.na(seq_mat$learn_ori_steps) ~ 30,
    
    seq_mat$learn_block == 1 & seq_mat$learn_stim_type == "hostile" & seq_mat$learn_trial_type == "standard" & seq_mat$learn_ori_steps == 1 ~   31,
    seq_mat$learn_block == 1 & seq_mat$learn_stim_type == "hostile" & seq_mat$learn_trial_type == "deviant" & seq_mat$learn_ori_steps == 1 ~  32,
    seq_mat$learn_block == 1 & seq_mat$learn_stim_type == "hostile" & seq_mat$learn_trial_type == "standard" & seq_mat$learn_ori_steps == 2 ~   33,
    seq_mat$learn_block == 1 & seq_mat$learn_stim_type == "hostile" & seq_mat$learn_trial_type == "deviant" & seq_mat$learn_ori_steps == 2 ~  34,
    seq_mat$learn_block == 1 & seq_mat$learn_stim_type == "hostile" & seq_mat$learn_trial_type == "standard" & seq_mat$learn_ori_steps == 3 ~   35,
    seq_mat$learn_block == 1 & seq_mat$learn_stim_type == "hostile" & seq_mat$learn_trial_type == "deviant" & seq_mat$learn_ori_steps == 3 ~  36,
    seq_mat$learn_block == 1 & seq_mat$learn_stim_type == "friendly" & seq_mat$learn_trial_type == "standard" & seq_mat$learn_ori_steps == 1 ~  37,
    seq_mat$learn_block == 1 & seq_mat$learn_stim_type == "friendly" & seq_mat$learn_trial_type == "deviant" & seq_mat$learn_ori_steps == 1 ~ 38,
    seq_mat$learn_block == 1 & seq_mat$learn_stim_type == "friendly" & seq_mat$learn_trial_type == "standard" & seq_mat$learn_ori_steps == 2 ~  39,
    seq_mat$learn_block == 1 & seq_mat$learn_stim_type == "friendly" & seq_mat$learn_trial_type == "deviant" & seq_mat$learn_ori_steps == 2 ~ 40,
    seq_mat$learn_block == 1 & seq_mat$learn_stim_type == "friendly" & seq_mat$learn_trial_type == "standard" & seq_mat$learn_ori_steps == 3 ~  41,
    seq_mat$learn_block == 1 & seq_mat$learn_stim_type == "friendly" & seq_mat$learn_trial_type == "deviant" & seq_mat$learn_ori_steps == 3 ~ 42,
    #block 2
    seq_mat$learn_block == 2 & seq_mat$learn_stim_type == "hostile" & seq_mat$learn_trial_type == "standard" & seq_mat$learn_ori_steps == 1 ~   43,
    seq_mat$learn_block == 2 & seq_mat$learn_stim_type == "hostile" & seq_mat$learn_trial_type == "deviant" & seq_mat$learn_ori_steps == 1 ~  44,
    seq_mat$learn_block == 2 & seq_mat$learn_stim_type == "hostile" & seq_mat$learn_trial_type == "standard" & seq_mat$learn_ori_steps == 2 ~   45,
    seq_mat$learn_block == 2 & seq_mat$learn_stim_type == "hostile" & seq_mat$learn_trial_type == "deviant" & seq_mat$learn_ori_steps == 2 ~  46,
    seq_mat$learn_block == 2 & seq_mat$learn_stim_type == "hostile" & seq_mat$learn_trial_type == "standard" & seq_mat$learn_ori_steps == 3 ~   47,
    seq_mat$learn_block == 2 & seq_mat$learn_stim_type == "hostile" & seq_mat$learn_trial_type == "deviant" & seq_mat$learn_ori_steps == 3 ~  48,
    seq_mat$learn_block == 2 & seq_mat$learn_stim_type == "friendly" & seq_mat$learn_trial_type == "standard" & seq_mat$learn_ori_steps == 1 ~  49,
    seq_mat$learn_block == 2 & seq_mat$learn_stim_type == "friendly" & seq_mat$learn_trial_type == "deviant" & seq_mat$learn_ori_steps == 1 ~ 50,
    seq_mat$learn_block == 2 & seq_mat$learn_stim_type == "friendly" & seq_mat$learn_trial_type == "standard" & seq_mat$learn_ori_steps == 2 ~  51,
    seq_mat$learn_block == 2 & seq_mat$learn_stim_type == "friendly" & seq_mat$learn_trial_type == "deviant" & seq_mat$learn_ori_steps == 2 ~ 52,
    seq_mat$learn_block == 2 & seq_mat$learn_stim_type == "friendly" & seq_mat$learn_trial_type == "standard" & seq_mat$learn_ori_steps == 3 ~  53,
    seq_mat$learn_block == 2 & seq_mat$learn_stim_type == "friendly" & seq_mat$learn_trial_type == "deviant" & seq_mat$learn_ori_steps == 3 ~ 54,
    #block 3
    seq_mat$learn_block == 3 & seq_mat$learn_stim_type == "hostile" & seq_mat$learn_trial_type == "standard" & seq_mat$learn_ori_steps == 1 ~   55,
    seq_mat$learn_block == 3 & seq_mat$learn_stim_type == "hostile" & seq_mat$learn_trial_type == "deviant" & seq_mat$learn_ori_steps == 1 ~  56,
    seq_mat$learn_block == 3 & seq_mat$learn_stim_type == "hostile" & seq_mat$learn_trial_type == "standard" & seq_mat$learn_ori_steps == 2 ~   57,
    seq_mat$learn_block == 3 & seq_mat$learn_stim_type == "hostile" & seq_mat$learn_trial_type == "deviant" & seq_mat$learn_ori_steps == 2 ~  58,
    seq_mat$learn_block == 3 & seq_mat$learn_stim_type == "hostile" & seq_mat$learn_trial_type == "standard" & seq_mat$learn_ori_steps == 3 ~   59,
    seq_mat$learn_block == 3 & seq_mat$learn_stim_type == "hostile" & seq_mat$learn_trial_type == "deviant" & seq_mat$learn_ori_steps == 3 ~  60,
    seq_mat$learn_block == 3 & seq_mat$learn_stim_type == "friendly" & seq_mat$learn_trial_type == "standard" & seq_mat$learn_ori_steps == 1 ~  61,
    seq_mat$learn_block == 3 & seq_mat$learn_stim_type == "friendly" & seq_mat$learn_trial_type == "deviant" & seq_mat$learn_ori_steps == 1 ~ 62,
    seq_mat$learn_block == 3 & seq_mat$learn_stim_type == "friendly" & seq_mat$learn_trial_type == "standard" & seq_mat$learn_ori_steps == 2 ~  63,
    seq_mat$learn_block == 3 & seq_mat$learn_stim_type == "friendly" & seq_mat$learn_trial_type == "deviant" & seq_mat$learn_ori_steps == 2 ~ 64,
    seq_mat$learn_block == 3 & seq_mat$learn_stim_type == "friendly" & seq_mat$learn_trial_type == "standard" & seq_mat$learn_ori_steps == 3 ~  65,
    seq_mat$learn_block == 3 & seq_mat$learn_stim_type == "friendly" & seq_mat$learn_trial_type == "deviant" & seq_mat$learn_ori_steps == 3 ~ 66,
    #block 4
    seq_mat$learn_block == 4 & seq_mat$learn_stim_type == "hostile" & seq_mat$learn_trial_type == "standard" & seq_mat$learn_ori_steps == 1 ~   67,
    seq_mat$learn_block == 4 & seq_mat$learn_stim_type == "hostile" & seq_mat$learn_trial_type == "deviant" & seq_mat$learn_ori_steps == 1 ~  68,
    seq_mat$learn_block == 4 & seq_mat$learn_stim_type == "hostile" & seq_mat$learn_trial_type == "standard" & seq_mat$learn_ori_steps == 2 ~   69,
    seq_mat$learn_block == 4 & seq_mat$learn_stim_type == "hostile" & seq_mat$learn_trial_type == "deviant" & seq_mat$learn_ori_steps == 2 ~  70,
    seq_mat$learn_block == 4 & seq_mat$learn_stim_type == "hostile" & seq_mat$learn_trial_type == "standard" & seq_mat$learn_ori_steps == 3 ~   71,
    seq_mat$learn_block == 4 & seq_mat$learn_stim_type == "hostile" & seq_mat$learn_trial_type == "deviant" & seq_mat$learn_ori_steps == 3 ~  72,
    seq_mat$learn_block == 4 & seq_mat$learn_stim_type == "friendly" & seq_mat$learn_trial_type == "standard" & seq_mat$learn_ori_steps == 1 ~  73,
    seq_mat$learn_block == 4 & seq_mat$learn_stim_type == "friendly" & seq_mat$learn_trial_type == "deviant" & seq_mat$learn_ori_steps == 1 ~ 74,
    seq_mat$learn_block == 4 & seq_mat$learn_stim_type == "friendly" & seq_mat$learn_trial_type == "standard" & seq_mat$learn_ori_steps == 2 ~  75,
    seq_mat$learn_block == 4 & seq_mat$learn_stim_type == "friendly" & seq_mat$learn_trial_type == "deviant" & seq_mat$learn_ori_steps == 2 ~ 76,
    seq_mat$learn_block == 4 & seq_mat$learn_stim_type == "friendly" & seq_mat$learn_trial_type == "standard" & seq_mat$learn_ori_steps == 3 ~  77,
    seq_mat$learn_block == 4 & seq_mat$learn_stim_type == "friendly" & seq_mat$learn_trial_type == "deviant" & seq_mat$learn_ori_steps == 3 ~ 78,
    #block 5
    seq_mat$learn_block == 5 & seq_mat$learn_stim_type == "hostile" & seq_mat$learn_trial_type == "standard" & seq_mat$learn_ori_steps == 1 ~   79,
    seq_mat$learn_block == 5 & seq_mat$learn_stim_type == "hostile" & seq_mat$learn_trial_type == "deviant" & seq_mat$learn_ori_steps == 1 ~  80,
    seq_mat$learn_block == 5 & seq_mat$learn_stim_type == "hostile" & seq_mat$learn_trial_type == "standard" & seq_mat$learn_ori_steps == 2 ~   81,
    seq_mat$learn_block == 5 & seq_mat$learn_stim_type == "hostile" & seq_mat$learn_trial_type == "deviant" & seq_mat$learn_ori_steps == 2 ~  82,
    seq_mat$learn_block == 5 & seq_mat$learn_stim_type == "hostile" & seq_mat$learn_trial_type == "standard" & seq_mat$learn_ori_steps == 3 ~   83,
    seq_mat$learn_block == 5 & seq_mat$learn_stim_type == "hostile" & seq_mat$learn_trial_type == "deviant" & seq_mat$learn_ori_steps == 3 ~  84,
    seq_mat$learn_block == 5 & seq_mat$learn_stim_type == "friendly" & seq_mat$learn_trial_type == "standard" & seq_mat$learn_ori_steps == 1 ~  85,
    seq_mat$learn_block == 5 & seq_mat$learn_stim_type == "friendly" & seq_mat$learn_trial_type == "deviant" & seq_mat$learn_ori_steps == 1 ~ 86,
    seq_mat$learn_block == 5 & seq_mat$learn_stim_type == "friendly" & seq_mat$learn_trial_type == "standard" & seq_mat$learn_ori_steps == 2 ~  87,
    seq_mat$learn_block == 5 & seq_mat$learn_stim_type == "friendly" & seq_mat$learn_trial_type == "deviant" & seq_mat$learn_ori_steps == 2 ~ 88,
    seq_mat$learn_block == 5 & seq_mat$learn_stim_type == "friendly" & seq_mat$learn_trial_type == "standard" & seq_mat$learn_ori_steps == 3 ~  89,
    seq_mat$learn_block == 5 & seq_mat$learn_stim_type == "friendly" & seq_mat$learn_trial_type == "deviant" & seq_mat$learn_ori_steps == 3 ~ 90)
  
  seq_mat$learn_offtrig = case_when(
    seq_mat$learn_freq_lab == 1 & seq_mat$learn_ori_lab == 1 ~ 103,
    seq_mat$learn_freq_lab == 1 & seq_mat$learn_ori_lab == 2 ~ 104,
    seq_mat$learn_freq_lab == 1 & seq_mat$learn_ori_lab == 3 ~ 105,
    seq_mat$learn_freq_lab == 1 & seq_mat$learn_ori_lab == 4 ~ 106,
    seq_mat$learn_freq_lab == 1 & seq_mat$learn_ori_lab == 5 ~ 107,
    seq_mat$learn_freq_lab == 1 & seq_mat$learn_ori_lab == 6 ~ 108,
    seq_mat$learn_freq_lab == 1 & seq_mat$learn_ori_lab == 7 ~ 109,
    seq_mat$learn_freq_lab == 1 & seq_mat$learn_ori_lab == 8 ~ 110,
    
    seq_mat$learn_freq_lab == 2 & seq_mat$learn_ori_lab == 1 ~ 111,
    seq_mat$learn_freq_lab == 2 & seq_mat$learn_ori_lab == 2 ~ 112,
    seq_mat$learn_freq_lab == 2 & seq_mat$learn_ori_lab == 3 ~ 113,
    seq_mat$learn_freq_lab == 2 & seq_mat$learn_ori_lab == 4 ~ 114,
    seq_mat$learn_freq_lab == 2 & seq_mat$learn_ori_lab == 5 ~ 115,
    seq_mat$learn_freq_lab == 2 & seq_mat$learn_ori_lab == 6 ~ 116,
    seq_mat$learn_freq_lab == 2 & seq_mat$learn_ori_lab == 7 ~ 117,
    seq_mat$learn_freq_lab == 2 & seq_mat$learn_ori_lab == 8 ~ 118,
    
    seq_mat$learn_freq_lab == 3 & seq_mat$learn_ori_lab == 1 ~ 119,
    seq_mat$learn_freq_lab == 3 & seq_mat$learn_ori_lab == 2 ~ 120,
    seq_mat$learn_freq_lab == 3 & seq_mat$learn_ori_lab == 3 ~ 121,
    seq_mat$learn_freq_lab == 3 & seq_mat$learn_ori_lab == 4 ~ 122,
    seq_mat$learn_freq_lab == 3 & seq_mat$learn_ori_lab == 5 ~ 123,
    seq_mat$learn_freq_lab == 3 & seq_mat$learn_ori_lab == 6 ~ 124,
    seq_mat$learn_freq_lab == 3 & seq_mat$learn_ori_lab == 7 ~ 125,
    seq_mat$learn_freq_lab == 3 & seq_mat$learn_ori_lab == 8 ~ 126,
    
    seq_mat$learn_freq_lab == 4 & seq_mat$learn_ori_lab == 1 ~ 127,
    seq_mat$learn_freq_lab == 4 & seq_mat$learn_ori_lab == 2 ~ 128,
    seq_mat$learn_freq_lab == 4 & seq_mat$learn_ori_lab == 3 ~ 129,
    seq_mat$learn_freq_lab == 4 & seq_mat$learn_ori_lab == 4 ~ 130,
    seq_mat$learn_freq_lab == 4 & seq_mat$learn_ori_lab == 5 ~ 131,
    seq_mat$learn_freq_lab == 4 & seq_mat$learn_ori_lab == 6 ~ 132,
    seq_mat$learn_freq_lab == 4 & seq_mat$learn_ori_lab == 7 ~ 133,
    seq_mat$learn_freq_lab == 4 & seq_mat$learn_ori_lab == 8 ~ 134,
    
    seq_mat$learn_freq_lab == 5 & seq_mat$learn_ori_lab == 1 ~ 135,
    seq_mat$learn_freq_lab == 5 & seq_mat$learn_ori_lab == 2 ~ 136,
    seq_mat$learn_freq_lab == 5 & seq_mat$learn_ori_lab == 3 ~ 137,
    seq_mat$learn_freq_lab == 5 & seq_mat$learn_ori_lab == 4 ~ 138,
    seq_mat$learn_freq_lab == 5 & seq_mat$learn_ori_lab == 5 ~ 139,
    seq_mat$learn_freq_lab == 5 & seq_mat$learn_ori_lab == 6 ~ 140,
    seq_mat$learn_freq_lab == 5 & seq_mat$learn_ori_lab == 7 ~ 141,
    seq_mat$learn_freq_lab == 5 & seq_mat$learn_ori_lab == 8 ~ 142,
    
    seq_mat$learn_freq_lab == 6 & seq_mat$learn_ori_lab == 1 ~ 143,
    seq_mat$learn_freq_lab == 6 & seq_mat$learn_ori_lab == 2 ~ 144,
    seq_mat$learn_freq_lab == 6 & seq_mat$learn_ori_lab == 3 ~ 145,
    seq_mat$learn_freq_lab == 6 & seq_mat$learn_ori_lab == 4 ~ 146,
    seq_mat$learn_freq_lab == 6 & seq_mat$learn_ori_lab == 5 ~ 147,
    seq_mat$learn_freq_lab == 6 & seq_mat$learn_ori_lab == 6 ~ 148,
    seq_mat$learn_freq_lab == 6 & seq_mat$learn_ori_lab == 7 ~ 149,
    seq_mat$learn_freq_lab == 6 & seq_mat$learn_ori_lab == 8 ~ 150,
    
    seq_mat$learn_freq_lab == 7 & seq_mat$learn_ori_lab == 1 ~ 151,
    seq_mat$learn_freq_lab == 7 & seq_mat$learn_ori_lab == 2 ~ 152,
    seq_mat$learn_freq_lab == 7 & seq_mat$learn_ori_lab == 3 ~ 153,
    seq_mat$learn_freq_lab == 7 & seq_mat$learn_ori_lab == 4 ~ 154,
    seq_mat$learn_freq_lab == 7 & seq_mat$learn_ori_lab == 5 ~ 155,
    seq_mat$learn_freq_lab == 7 & seq_mat$learn_ori_lab == 6 ~ 156,
    seq_mat$learn_freq_lab == 7 & seq_mat$learn_ori_lab == 7 ~ 157,
    seq_mat$learn_freq_lab == 7 & seq_mat$learn_ori_lab == 8 ~ 158,
    
    seq_mat$learn_freq_lab == 8 & seq_mat$learn_ori_lab == 1 ~ 159,
    seq_mat$learn_freq_lab == 8 & seq_mat$learn_ori_lab == 2 ~ 160,
    seq_mat$learn_freq_lab == 8 & seq_mat$learn_ori_lab == 3 ~ 161,
    seq_mat$learn_freq_lab == 8 & seq_mat$learn_ori_lab == 4 ~ 162,
    seq_mat$learn_freq_lab == 8 & seq_mat$learn_ori_lab == 5 ~ 163,
    seq_mat$learn_freq_lab == 8 & seq_mat$learn_ori_lab == 6 ~ 164,
    seq_mat$learn_freq_lab == 8 & seq_mat$learn_ori_lab == 7 ~ 165,
    seq_mat$learn_freq_lab == 8 & seq_mat$learn_ori_lab == 8 ~ 166)
  
  return(seq_mat)
}

################################################################################

#set orientation values (see stimvals_experiment5 spreadsheet)
or1 <- -33.75
or2 <- -11.25
or3 <- 11.25
or4 <- 33.75
or5 <- 56.25
or6 <- 78.75
or7 <- -78.75
or8 <- -56.25

#set spatial frequency values (see stimvals_experiment5 spreadsheet)
sf1 <- 6
sf2 <- 6.72
sf3 <- 7.5264
sf4 <- 8.4297
sf5 <- 9.441
sf6 <- 10.5741
sf7 <- 11.8428
sf8 <- 13.2642

#create oddball high sequences
seq_oddhigh_1 <- sequenceR(transition_matrix = transMat_oddball_high, blocks = 5, oddball = 'high', seed = 1)
table(seq_oddhigh_1[,1])
table(seq_oddhigh_1[,2]) # make sure there are no 0 step transitions; the sequenceR function can very occasionally get cornered into them

seq_oddhigh_2 <- sequenceR(transition_matrix = transMat_oddball_high, blocks = 5, oddball = 'high', seed = 2)
table(seq_oddhigh_1[,1])
table(seq_oddhigh_1[,2]) # make sure there are no 0 step transitions

seq_oddhigh_3 <- sequenceR(transition_matrix = transMat_oddball_high, blocks = 5, oddball = 'high', seed = 3)
table(seq_oddhigh_1[,1])
table(seq_oddhigh_1[,2]) # make sure there are no 0 step transitions

seq_oddhigh_4 <- sequenceR(transition_matrix = transMat_oddball_high, blocks = 5, oddball = 'high', seed = 4)
table(seq_oddhigh_1[,1])
table(seq_oddhigh_1[,2]) # make sure there are no 0 step transitions

seq_oddhigh_5 <- sequenceR(transition_matrix = transMat_oddball_high, blocks = 5, oddball = 'high', seed = 5)
table(seq_oddhigh_1[,1])
table(seq_oddhigh_1[,2]) # make sure there are no 0 step transitions

#create oddball low sequences
seq_oddlow_1 <- sequenceR(transition_matrix = transMat_oddball_low, blocks = 5, oddball = 'low', seed = 1)
table(seq_oddlow_1[,1])
table(seq_oddlow_1[,2])

seq_oddlow_2 <- sequenceR(transition_matrix = transMat_oddball_low, blocks = 5, oddball = 'low', seed = 2)
table(seq_oddlow_2[,1])
table(seq_oddlow_2[,2])

seq_oddlow_3 <- sequenceR(transition_matrix = transMat_oddball_low, blocks = 5, oddball = 'low', seed = 3)
table(seq_oddlow_3[,1])
table(seq_oddlow_3[,2])

seq_oddlow_4 <- sequenceR(transition_matrix = transMat_oddball_low, blocks = 5, oddball = 'low', seed = 4)
table(seq_oddlow_4[,1])
table(seq_oddlow_4[,2])

seq_oddlow_5 <- sequenceR(transition_matrix = transMat_oddball_low, blocks = 5, oddball = 'low', seed = 6) #seed 5 generates a sequence that includes a 0-step
table(seq_oddlow_5[,1])
table(seq_oddlow_5[,2])

#create conditions files using created sequences
cond_oddhigh_1 <- seq_to_cond(seq_oddhigh_1, seed = 22, oddball = 'high',
                              or1, or2, or3, or4, or5, or6, or7, or8,
                              sf1, sf2, sf3, sf4, sf5, sf6, sf7, sf8)
table(cond_oddhigh_1$learn_block, cond_oddhigh_1$learn_ori_val) #ori balancing in each block
table(cond_oddhigh_1$learn_block, cond_oddhigh_1$learn_freq_val) #freq balancing in each block
table(cond_oddhigh_1$learn_block, cond_oddhigh_1$learn_trial_type) #oddball balancing in each block
table(cond_oddhigh_1$learn_block, cond_oddhigh_1$learn_pos_lab) #explorer position balancing in each block
table(cond_oddhigh_1$learn_freq_val, cond_oddhigh_1$learn_trial_type) #trial type balancing for each trial type

cond_oddhigh_2 <- seq_to_cond(seq_oddhigh_2, seed = 22, oddball = 'high',
                              or1, or2, or3, or4, or5, or6, or7, or8,
                              sf1, sf2, sf3, sf4, sf5, sf6, sf7, sf8)
table(cond_oddhigh_2$learn_block, cond_oddhigh_2$learn_ori_val) #ori balancing in each block
table(cond_oddhigh_2$learn_block, cond_oddhigh_2$learn_freq_val) #freq balancing in each block
table(cond_oddhigh_2$learn_block, cond_oddhigh_2$learn_trial_type) #oddball balancing in each block
table(cond_oddhigh_2$learn_block, cond_oddhigh_2$learn_pos_lab) #explorer position balancing in each block
table(cond_oddhigh_2$learn_freq_val, cond_oddhigh_2$learn_trial_type) #trial type balancing for each trial type

cond_oddhigh_3 <- seq_to_cond(seq_oddhigh_3, seed = 22, oddball = 'high',
                              or1, or2, or3, or4, or5, or6, or7, or8,
                              sf1, sf2, sf3, sf4, sf5, sf6, sf7, sf8)
table(cond_oddhigh_3$learn_block, cond_oddhigh_3$learn_ori_val) #ori balancing in each block
table(cond_oddhigh_3$learn_block, cond_oddhigh_3$learn_freq_val) #freq balancing in each block
table(cond_oddhigh_3$learn_block, cond_oddhigh_3$learn_trial_type) #oddball balancing in each block
table(cond_oddhigh_3$learn_block, cond_oddhigh_3$learn_pos_lab) #explorer position balancing in each block
table(cond_oddhigh_3$learn_freq_val, cond_oddhigh_3$learn_trial_type) #trial type balancing for each trial type

cond_oddhigh_4 <- seq_to_cond(seq_oddhigh_4, seed = 22, oddball = 'high',
                              or1, or2, or3, or4, or5, or6, or7, or8,
                              sf1, sf2, sf3, sf4, sf5, sf6, sf7, sf8)
table(cond_oddhigh_4$learn_block, cond_oddhigh_4$learn_ori_val) #ori balancing in each block
table(cond_oddhigh_4$learn_block, cond_oddhigh_4$learn_freq_val) #freq balancing in each block
table(cond_oddhigh_4$learn_block, cond_oddhigh_4$learn_trial_type) #oddball balancing in each block
table(cond_oddhigh_4$learn_block, cond_oddhigh_4$learn_pos_lab) #explorer position balancing in each block
table(cond_oddhigh_4$learn_freq_val, cond_oddhigh_4$learn_trial_type) #trial type balancing for each trial type

cond_oddhigh_5 <- seq_to_cond(seq_oddhigh_5, seed = 22, oddball = 'high',
                              or1, or2, or3, or4, or5, or6, or7, or8,
                              sf1, sf2, sf3, sf4, sf5, sf6, sf7, sf8)
table(cond_oddhigh_5$learn_block, cond_oddhigh_5$learn_ori_val) #ori balancing in each block
table(cond_oddhigh_5$learn_block, cond_oddhigh_5$learn_freq_val) #freq balancing in each block
table(cond_oddhigh_5$learn_block, cond_oddhigh_5$learn_trial_type) #oddball balancing in each block
table(cond_oddhigh_5$learn_block, cond_oddhigh_5$learn_pos_lab) #explorer position balancing in each block
table(cond_oddhigh_5$learn_freq_val, cond_oddhigh_5$learn_trial_type) #trial type balancing for each trial type

cond_oddlow_1 <- seq_to_cond(seq_oddlow_1, seed = 22, oddball = 'low',
                              or1, or2, or3, or4, or5, or6, or7, or8,
                              sf1, sf2, sf3, sf4, sf5, sf6, sf7, sf8)
table(cond_oddlow_1$learn_block, cond_oddlow_1$learn_ori_val) #ori balancing in each block
table(cond_oddlow_1$learn_block, cond_oddlow_1$learn_freq_val) #freq balancing in each block
table(cond_oddlow_1$learn_block, cond_oddlow_1$learn_trial_type) #oddball balancing in each block
table(cond_oddlow_1$learn_block, cond_oddlow_1$learn_pos_lab) #explorer position balancing in each block
table(cond_oddlow_1$learn_freq_val, cond_oddlow_1$learn_trial_type) #trial type balancing for each trial type

cond_oddlow_2 <- seq_to_cond(seq_oddlow_2, seed = 22, oddball = 'low',
                             or1, or2, or3, or4, or5, or6, or7, or8,
                             sf1, sf2, sf3, sf4, sf5, sf6, sf7, sf8)
table(cond_oddlow_2$learn_block, cond_oddlow_2$learn_ori_val) #ori balancing in each block
table(cond_oddlow_2$learn_block, cond_oddlow_2$learn_freq_val) #freq balancing in each block
table(cond_oddlow_2$learn_block, cond_oddlow_2$learn_trial_type) #oddball balancing in each block
table(cond_oddlow_2$learn_block, cond_oddlow_2$learn_pos_lab) #explorer position balancing in each block
table(cond_oddlow_2$learn_freq_val, cond_oddlow_2$learn_trial_type) #trial type balancing for each trial type

cond_oddlow_3 <- seq_to_cond(seq_oddlow_3, seed = 22, oddball = 'low',
                             or1, or2, or3, or4, or5, or6, or7, or8,
                             sf1, sf2, sf3, sf4, sf5, sf6, sf7, sf8)
table(cond_oddlow_3$learn_block, cond_oddlow_3$learn_ori_val) #ori balancing in each block
table(cond_oddlow_3$learn_block, cond_oddlow_3$learn_freq_val) #freq balancing in each block
table(cond_oddlow_3$learn_block, cond_oddlow_3$learn_trial_type) #oddball balancing in each block
table(cond_oddlow_3$learn_block, cond_oddlow_3$learn_pos_lab) #explorer position balancing in each block
table(cond_oddlow_3$learn_freq_val, cond_oddlow_3$learn_trial_type) #trial type balancing for each trial type

cond_oddlow_4 <- seq_to_cond(seq_oddlow_4, seed = 22, oddball = 'low',
                             or1, or2, or3, or4, or5, or6, or7, or8,
                             sf1, sf2, sf3, sf4, sf5, sf6, sf7, sf8)
table(cond_oddlow_4$learn_block, cond_oddlow_4$learn_ori_val) #ori balancing in each block
table(cond_oddlow_4$learn_block, cond_oddlow_4$learn_freq_val) #freq balancing in each block
table(cond_oddlow_4$learn_block, cond_oddlow_4$learn_trial_type) #oddball balancing in each block
table(cond_oddlow_4$learn_block, cond_oddlow_4$learn_pos_lab) #explorer position balancing in each block
table(cond_oddlow_4$learn_freq_val, cond_oddlow_4$learn_trial_type) #trial type balancing for each trial type

cond_oddlow_5 <- seq_to_cond(seq_oddlow_5, seed = 22, oddball = 'low',
                             or1, or2, or3, or4, or5, or6, or7, or8,
                             sf1, sf2, sf3, sf4, sf5, sf6, sf7, sf8)
table(cond_oddlow_5$learn_block, cond_oddlow_5$learn_ori_val) #ori balancing in each block
table(cond_oddlow_5$learn_block, cond_oddlow_5$learn_freq_val) #freq balancing in each block
table(cond_oddlow_5$learn_block, cond_oddlow_5$learn_trial_type) #oddball balancing in each block
table(cond_oddlow_5$learn_block, cond_oddlow_5$learn_pos_lab) #explorer position balancing in each block
table(cond_oddlow_5$learn_freq_val, cond_oddlow_5$learn_trial_type) #trial type balancing for each trial type

#if all looks good, write them out:
#write.xlsx(cond_oddhigh_1, "cond_oddhigh_1_out.xlsx", rowNames = F)
#write.xlsx(cond_oddhigh_2, "cond_oddhigh_2_out.xlsx", rowNames = F)
#write.xlsx(cond_oddhigh_3, "cond_oddhigh_3_out.xlsx", rowNames = F)
#write.xlsx(cond_oddhigh_4, "cond_oddhigh_4_out.xlsx", rowNames = F)
#write.xlsx(cond_oddhigh_5, "cond_oddhigh_5_out.xlsx", rowNames = F)
#write.xlsx(cond_oddlow_1, "cond_oddlow_1_out.xlsx", rowNames = F)
#write.xlsx(cond_oddlow_2, "cond_oddlow_2_out.xlsx", rowNames = F)
#write.xlsx(cond_oddlow_3, "cond_oddlow_3_out.xlsx", rowNames = F)
#write.xlsx(cond_oddlow_4, "cond_oddlow_4_out.xlsx", rowNames = F)
#write.xlsx(cond_oddlow_5, "cond_oddlow_5_out.xlsx", rowNames = F)
###NOTE: THESE FILES DO NOT WORK IF USED DIRECTLY IN PSYCHOPY - WILL GET ERROR "There is no item named 'xl/drawings/drawing1.xml' in the archive"
###NEED TO OPEN EACH IN EXCEL, SAVE A COPY IN THE CONDITIONS FOLDER, AND THEN THEY WILL WORK
