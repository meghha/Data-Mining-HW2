# Answer found in Q5 in Question Bank 1 (Tan et al, 2nd ed)

# import student_code_with_answers.utils as u
import utils as u


# Example of how to specify a binary with the structure:
# See the file INSTRUCTIONS.md
# ----------------------------------------------------------------------


def question1():
    """
    Note 1: Each attribute can appear as a node in the tree AT MOST once.
    Note 2: For level two, fill the keys for all cases left and right. If and attribute
    is not considered for level 2, set the values to -1. For example, if "flu" were the
    choice for level 1 (it is not), then set level2_left['flu'] = level2_right['flu'] = -1.,
    and the same for keys 'flu_info_gain'.
    """
    answer = False
    answer = {}
    level1 = {}
    level2_left = {}
    level2_right = {}

    nb_y = 5
    nb_n = 5
    ntot = nb_y + nb_n
    H = -(nb_y/ntot * u.log2(nb_y/ntot) + nb_n/ntot * u.log2(nb_n/ntot))

    smoking_y_y = 4
    smoking_y_n = 1
    smoking_n_y = 1
    smoking_n_n = 4
    smoking_y_tot =  smoking_y_y + smoking_y_n
    smoking_n_tot =  smoking_n_y + smoking_n_n
    smoking_tot = smoking_y_tot + smoking_n_tot
    entropy_y = -(smoking_y_y/smoking_y_tot * u.log2(smoking_y_y/smoking_y_tot) + smoking_y_n/smoking_y_tot * u.log2(smoking_y_n/smoking_y_tot))
    entropy_n = -(smoking_n_y/smoking_n_tot * u.log2(smoking_n_y/smoking_n_tot) + smoking_n_n/smoking_n_tot * u.log2(smoking_n_n/smoking_n_tot))
    weighted_entropy_smoking = (smoking_y_tot/smoking_tot * (entropy_y)) + (smoking_n_tot/smoking_tot * (entropy_n))
    
    level1["smoking"] = 0.72
    level1["smoking_info_gain"] = 0.28

    cough_y_y = 4
    cough_y_n = 1
    cough_n_y = 1
    cough_n_n = 4
    cough_y_tot =  cough_y_y + cough_y_n
    cough_n_tot =  cough_n_y + cough_n_n
    cough_tot = cough_y_tot + cough_n_tot
    entropy_y = -(cough_y_y/cough_y_tot * u.log2(cough_y_y/cough_y_tot) + cough_y_n/cough_y_tot * u.log2(cough_y_n/cough_y_tot))
    entropy_n = -(cough_n_y/cough_n_tot * u.log2(cough_n_y/cough_n_tot) + cough_n_n/cough_n_tot * u.log2(cough_n_n/cough_n_tot))
    weighted_entropy_cough = (cough_y_tot/cough_tot * (entropy_y)) + (cough_n_tot/cough_tot * (entropy_n))

    level1["cough"] = 0.97
    level1["cough_info_gain"] = 0.03

    radon_y_y = 4
    radon_y_n = 3
    radon_n_y = 1
    radon_n_n = 2
    radon_y_tot =  radon_y_y + radon_y_n
    radon_n_tot =  radon_n_y + radon_n_n
    radon_tot = radon_y_tot + radon_n_tot
    entropy_y = -(radon_y_y/radon_y_tot * u.log2(radon_y_y/radon_y_tot) + radon_y_n/radon_y_tot * u.log2(radon_y_n/radon_y_tot))
    entropy_n = -(radon_n_y/radon_n_tot * u.log2(radon_n_y/radon_n_tot) + radon_n_n/radon_n_tot * u.log2(radon_n_n/radon_n_tot))
    weighted_entropy_radon = (radon_y_tot/radon_tot * (entropy_y)) + (radon_n_tot/radon_tot * (entropy_n))
    
    level1["radon"] = 0.76
    level1["radon_info_gain"] = 0.24

    weight_loss_y_y = 4
    weight_loss_y_n = 1
    weight_loss_n_y = 1
    weight_loss_n_n = 4
    weight_loss_y_tot =  weight_loss_y_y + weight_loss_y_n
    weight_loss_n_tot =  weight_loss_n_y + weight_loss_n_n
    weight_loss_tot = weight_loss_y_tot + weight_loss_n_tot
    entropy_y = -(weight_loss_y_y/weight_loss_y_tot * u.log2(weight_loss_y_y/weight_loss_y_tot) + weight_loss_y_n/weight_loss_y_tot * u.log2(weight_loss_y_n/weight_loss_y_tot))
    entropy_n = -(weight_loss_n_y/weight_loss_n_tot * u.log2(weight_loss_n_y/weight_loss_n_tot) + weight_loss_n_n/weight_loss_n_tot * u.log2(weight_loss_n_n/weight_loss_n_tot))
    weighted_entropy_weight_loss = (weight_loss_y_tot/weight_loss_tot * (entropy_y)) + (weight_loss_n_tot/weight_loss_tot * (entropy_n))

    level1["weight_loss"] = 0.97
    level1["weight_loss_info_gain"] = 0.03

    level2_left["smoking"] = -1
    level2_left["smoking_info_gain"] = -1
    level2_right["smoking"] = -1
    level2_right["smoking_info_gain"] = -1

    level2_left["radon"] = 0.649
    level2_left["radon_info_gain"] = 0.

    level2_left["cough"] = 
    level2_left["cough_info_gain"] = 0.

    level2_left["weight_loss"] = 0.
    level2_left["weight_loss_info_gain"] = 0.

    level2_right["radon"] = 0.0
    level2_right["radon_info_gain"] = 0.

    level2_right["cough"] = 0.
    level2_right["cough_info_gain"] = 0.

    level2_right["weight_loss"] = 0.
    level2_right["weight_loss_info_gain"] = 0.

    answer["level1"] = level1
    answer["level2_left"] = level2_left
    answer["level2_right"] = level2_right

    # Fill up `construct_tree``
    # tree, training_error = construct_tree()
    tree = u.BinaryTree("root")  # MUST STILL CREATE THE TREE *****
    answer["tree"] = tree  # use the Tree structure
    # answer["training_error"] = training_error
    answer["training_error"] = 0.0  

    return answer


# ----------------------------------------------------------------------


def question2():
    answer = {}

    # Answers are floats
    answer["(a) entropy_entire_data"] = 0.
    # Infogain
    answer["(b) x <= 0.2"] = 0.
    answer["(b) x <= 0.7"] = 0.
    answer["(b) y <= 0.6"] = 0.

    # choose one of 'x=0.2', 'x=0.7', or 'x=0.6'
    answer["(c) attribute"] = ""  

    # Use the Binary Tree structure to construct the tree
    # Answer is an instance of BinaryTree
    tree = u.BinaryTree("Root")
    answer["(d) full decision tree"] = tree

    return answer


# ----------------------------------------------------------------------


def question3():
    answer = {}

    # float
    answer["(a) Gini, overall"] = 0.5

    # float
    answer["(b) Gini, ID"] = 0.0
    answer["(c) Gini, Gender"] = 0.48
    answer["(d) Gini, Car type"] = 0.1625
    answer["(e) Gini, Shirt type"] = 0.4914

    answer["(f) attr for splitting"] = "Car type"

    # Explanatory text string
    answer["(f) explain choice"] = "I will use Car type attribute to split at the root node, as it has the lowest Gini index or impurity. In other words, as the Gini index quantifies purity of an attribute or set of attributes, such that 0 expresses perfect equality (all elements belong to the same class) and 1 expresses maximal inequality (elements are randomly distributed across various classes), we should choose an attribute that has the lowest Gini."

    return answer


# ----------------------------------------------------------------------
# Answers in th form [str1, str2, str3]
# If both 'binary' and 'discrete' apply, choose 'binary'.
# str1 in ['binary', 'discrete', 'continuous']
# str2 in ['qualitative', 'quantitative']
# str3 in ['interval', 'nominal', 'ratio', 'ordinal']


def question4():
    answer = {}

    # [string, string, string]
    # Each string is one of ['binary', 'discrete', 'continuous', 'qualitative', 'nominal', 'ordinal',
    #  'quantitative', 'interval', 'ratio'
    # If you have a choice between 'binary' and 'discrete', choose 'binary'

    answer["a"] = ['binary','qualititative','nominal']

    # Explain if there is more than one interpretation. Repeat for the other questions. At least five words that form a sentence.
    answer["a: explain"] = ""

    answer["b"] = ['continuous','quantitative','ratio']
    answer["b: explain"] = ""

    answer["c"] = ['discrete','qualitative','ordinal']
    answer["c: explain"] = ""

    answer["d"] = ['continuous','quantitative','ratio']
    answer["d: explain"] = ""

    answer["e"] = ['discrete','qualitative','ordinal']
    answer["e: explain"] = ""

    answer["f"] = ['continuous','quantitative','ratio']
    answer["f: explain"] = ""

    answer["g"] = ['discrete','qualitative','nominal']
    answer["g: explain"] = ""

    answer["h"] = ['discrete','quantitative','ratio']
    answer["h: explain"] = ""

    answer["i"] = ['discrete','qualitative','nominal']
    answer["i: explain"] = ""

    answer["j"] = ['discrete','qualitative','ordinal']
    answer["j: explain"] = ""

    answer["k"] = ['continuous','quantitative','interval']
    answer["k: explain"] = ""

    answer["l"] = ['continuous','quantitative','ratio']
    answer["l: explain"] = ""

    answer["m"] = ['discrete','qualitative','nominal']
    answer["m: explain"] = ""

    return answer


# ----------------------------------------------------------------------


def question5():
    explain = {}

    # Read appropriate section of book chapter 3

    # string: one of 'Model 1' or 'Model 2'
    explain["a"] = "Model 2"
    explain["a explain"] = "Model 2, because it does not exhibit any overfitting, as compared to model 1. Therefore it can be generalised well to unseen data, as its accuracy is higher. The reason for such overfitting in Model 1 is that it is not pruned and the tree is allowed to grow until all the observations occupy leaf nodes."

    # string: one of 'Model 1' or 'Model 2'
    explain["b"] = "Model 2"
    explain["b explain"] = "There is still a fair bit of overfitting observed for model 1, because there is a huge difference in the train and test accuracy. This means the model still cannot generalise well to unseen data."

    explain["c similarity"] = "Both models employ techniques to minimize model complexity. \"
    explain["c similarity explain"] = ""

    explain["c difference"] = "While MDL seeks to find the simplest model, by minimizing the amount of encoding needed to describe the model and data, Pessimistic error estimate aims to reduce the model complexity, by penalizing the error produced by the nodes in decision tree, it penalizes nodes if the error due to the addition of a node is more than the error due to one training error as a result of that node."
    explain["c difference explain"] = ""

    return explain


# ----------------------------------------------------------------------
def question6():
    answer = {}
    # x <= ? is the left branch
    # y <= ? is the left branch

    # value of the form "z <= float" where "z" is "x" or "y"
    #  and "float" is a floating point number (notice: <=)
    # The value could also be "A" or "B" if it is a leaf
    answer["a, level 1"] = ""
    answer["a, level 2, right"] =""
    answer["a, level 2, left"] = ""
    answer["a, level 3, left"] = ""
    answer["a, level 3, right"] = ""

    # run each datum through the tree. Count the number of errors and divide by number of samples. .
    # Since we have areas: calculate the area that is misclassified (total area is unity)
    # float between 0 and 1
    answer["b, expected error"] = 0.

    # Use u.BinaryTree to define the tree. Create your tree.
    # Replace "root node" by the proper node of the form "z <= float"
    tree = u.BinaryTree("root note")

    answer["c, tree"] = tree

    return answer


# ----------------------------------------------------------------------
def question7():
    answer = {}

    # float
    answer["a, info gain, ID"] = 1
    answer["b, info gain, Handedness"] = 0.539

    # string: "ID" or "Handedness"
    answer["c, which attrib"] = "ID"

    # answer is a float
    answer["d, gain ratio, ID"] = 1
    answer["e, gain ratio, Handedness"] = 1.1322

    # string: one of 'ID' or 'Handedness' based on gain ratio
    # choose the attribute with the largest gain ratio
    answer["f, which attrib"] = "Handedness"

    return answer


# ----------------------------------------------------------------------

if __name__ == "__main__":
    answers = {}
    answers["q1"] = question1()
    answers["q2"] = question2()
    answers["q3"] = question3()
    answers["q4"] = question4()
    answers["q5"] = question5()
    answers["q6"] = question6()
    answers["q7"] = question7()

    u.save_dict("answers.pkl", answers)

