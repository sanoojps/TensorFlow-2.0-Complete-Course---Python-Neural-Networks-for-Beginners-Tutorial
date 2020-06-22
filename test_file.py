import tensorflow as tf
from DEBUG import debug

# deals with tensors
# multidimensional arrays
# has a rank -> determined by the number of dimensions
# A tensor is a container which can house data in N dimensions, 
# along with its linear operations, 
# though there is nuance in what tensors technically are
# and what we refer to as tensors in practice.
# 
# Source
# ------
# https://www.kdnuggets.com/2018/05/wtf-tensor.html
# 

# RANK
# #####
# rank 1
# list inside list
# multi dimensional array
# rank = number of dimensions

string = tf.Variable("Test",tf.string)
debug(string)
number = tf.Variable(125,tf.int16)
float = tf.Variable(1.11,tf.float64)

# find ranks
debug(
    "rank of string scalar {}".format(tf.rank(string))
) 
# rank of string scalar Tensor("Rank:0", shape=(), dtype=int32)
#     
# rank 0 -> SCALAR
# rank 1 -> VECTOR
# rank 2 -> MATRIX
# rank N -> TENSOR

rank_1_tensor = tf.Variable(["rank_1_tensor"],tf.string)
debug(tf.rank(rank_1_tensor))
# Tensor("Rank_1:0", shape=(), dtype=int32)

rank_2_tensor = tf.Variable(["rank_1_tensor",["OK"]],tf.string)
debug(tf.rank(rank_2_tensor))
# Tensor("Rank_2:0", shape=(), dtype=int32)

rank_3_tensor = tf.Variable(
    [
        ["rank_1_tensor","OK"],
        ["rank_1_tensor","OK"]
    ],
    tf.string
    )
debug(tf.rank(rank_3_tensor))
# Tensor("Rank_3:0", shape=(), dtype=int32)

# SHAPE
#######
# How many items in each dimension
shape_of_rank_2_tensor = tf.shape(rank_2_tensor)
debug(shape_of_rank_2_tensor)
# Tensor("Shape:0", shape=(1,), dtype=int32)
shape_of_rank_3_tensor = tf.shape(rank_3_tensor)
debug(shape_of_rank_2_tensor)