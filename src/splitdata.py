import numpy as np



def get_train_test_inds(y):

    train_inds = y.sample(frac=0.8, random_state=1)
    test_inds = y.drop(train_inds.index)

    return train_inds, test_inds



    #y=np.array(y)
    #train_inds = np.zeros(len(y),dtype=bool)
    #test_inds = np.zeros(len(y),dtype=bool)
    #values = np.unique(y)
    #for value in values:
    #    value_inds = np.nonzero(y==value)[0]
     #   np.random.shuffle(value_inds)
      #  n = int(train_proportion*len(value_inds))

       # train_inds[value_inds[:n]]=True
       # test_inds[value_inds[n:]]=True






