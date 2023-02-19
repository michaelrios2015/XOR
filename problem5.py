import math
import random

# step one lets see if I can forward propogate one and check for error

# step two do it for all four

# step three start tackiling back propagation

# so I have my XOR truth table and that is one of the main things to start with
# these do not include the answers
#  I think prof used something like input_1 = ([1, 1], 0 ) but can't really remember an array should be fine for the moment

input_1 = [0, 0, 0]

input_2 = [0, 1, 1]

input_3 = [1, 0, 1]

input_4 = [1, 1, 0]

# so I can loop through

inputs = [input_1, input_2, input_3, input_4]

# I also have 9 weights
# will be using random.uniform unseeded or some such

# biases
# does one layer usually have two biases I thought it was one bias and then a different weight for each neuron it goes to

b1 = b2 = bb1 = 1

# print(f'b1 = {b1}')

# my six
wij_11 = random.uniform(-1, 1)

# print(wij_11)

wij_12 = random.uniform(-1, 1)

# print(wij_12)

wij_21 = random.uniform(-1, 1)

# print(wij_21)

wij_22 = random.uniform(-1, 1)

# print(wij_22)

wjk_11 = random.uniform(-1, 1)

# print(wjk_11)

wjk_21 = random.uniform(-1, 1)

# print(wjk_21)

# bias weights

wb1 = random.uniform(-1, 1)

wb2 = random.uniform(-1, 1)

wbb1 = random.uniform(-1, 1)


# eta

eta = .1

error = 100

# while error > 1.1:

for x in range(100):

    # will use this to store all my targets and predictions
    y_k = []

    error = 0

    random.shuffle(inputs)

    # will run all the forward propagation
    for i in inputs:

        # print(i)
        # strictly the input
        z1 = i[0]

        # print(f'z1 = {z1}')

        z2 = i[1]

        # print(f'z2 = {z2}')

        # our target value
        t_1 = i[2]

        # print(f't_1 = {t_1}')

        # making the hidden layer

        # STEO ONE SUM

        net_output_1 = b1 * wb1 + z1 * wij_11 + z2 * wij_21

        net_output_2 = b2 * wb2 + z1 * wij_12 + z2 * wij_22

        # print(f'\nnet_output1: {net_output_1}  \n')

        # print(f'net_output2: {net_output_2}  \n')

        # SIGMOID FUNCTIONS

        zz1 = 1/(1 + math.exp(-net_output_1))
        zz2 = 1/(1 + math.exp(-net_output_2))

        # print(f'zz1 = {zz1}\n')

        # print(f'zz2 = {zz2}\n')

        # OUTPUT LAYER SUM

        net_output_final = bb1 * wbb1 + zz1 * wjk_11 + zz2 * wjk_21

        # print(f'\nnet_output1: {net_output_final}  \n')

        # SIGMOID FUNCTION FINAL LAYER

        y1 = 1/(1 + math.exp(-net_output_final))

        y_k.append([t_1, y1])

        #  seems to be working :)
        print(f't1 = {t_1} & y1 = {y1}\n')

        # ERROR
        error = error + .5 * pow((t_1 - y1), 2)

    # will run all the backward propagation
    for j in y_k:

        # print(f'j = {j}')
        t_1 = j[0]

        y_1 = j[1]

        print(f't_1= {t_1} and y_1= {y_1}')

        # print(f'error = {error}\n')

        # DELTA K --- is this supposed to be in the same for loop... maybe I run all the data and adjust afterwards
        # so delta k will change the weights of all the hideen layer weights
        delta_k1 = y1 * (1 - y1) * (t_1 - y1)

        # print(f'delta_k1 = {delta_k1}\n')

        # the delta_js change the input layer weights
        # delta_j1 for the weights going to j1 (1,1) (2,1) + the bias weight

        delta_j1 = zz1 * (1 - zz1) * (wjk_11 * delta_k1)

        # delta_j1 = zz1 * (1 - zz1) * (delta_k1) * (wjk_11 + wjk_21)

        # print(f'delta_j1 = {delta_j1}\n')

        # deltaj2 for those going to j2 (1,2) (2,2) and the bias weight

        delta_j2 = zz2 * (1-zz2) * (wjk_21 * delta_k1)

        # delta_j2 = zz2 * (1-zz2) * (delta_k1) * (wjk_11 + wjk_21)

        # print(f'delta_j2 = {delta_j2}\n')

        # now we calculate the changes to the weights and update them

        delta_wjk_11 = eta * zz1 * delta_k1

        # print(f'delta_wjk_11 = {delta_wjk_11}\n')

        delta_wjk_21 = eta * zz2 * delta_k1

        # print(f'delta_wjk_21 = {delta_wjk_21}\n')

        # pretty sure this is the right formula, as we don't seem to to be using the weights in the pervious 2 formulas
        delta_wbb1 = eta * bb1 * delta_k1

        # print(f'delta_wbb1 = {delta_wbb1}\n')

        # Update the weights
        wjk_11 += delta_wjk_11

        # print(f'wjk_11 = {wjk_11}\n')

        wjk_21 += delta_wjk_21

        # print(f'wjk_21 = {wjk_21}\n')

        wbb1 += delta_wbb1

        # print(f'wbb1 = {wbb1}\n')

        # calvulating delta for j1 weights

        delta_wij_11 = eta * z1 * delta_j1

        # print(f'delta_wij_11 = {delta_wij_11}\n')

        delta_wij_21 = eta * z2 * delta_j1

        # print(f'delta_wij_21 = {delta_wij_21}\n')

        # pretty sure this is the right formula, as we don't seem to to be using the weights in the pervious 2 formulas
        delta_wb1 = eta * b1 * delta_j1

        # print(f'delta_wb1 = {delta_wb1}\n')

        # Update the weights for j1
        wij_11 += delta_wij_11

        # print(f'wij_11 = {wij_11}\n')

        wij_21 += delta_wij_21

        # print(f'wij_21 = {wij_21}\n')

        wb1 += delta_wb1

        # print(f'wb1 = {wb1}\n')

        # calvulating delta for j2 weights

        delta_wij_12 = eta * z1 * delta_j2

        # print(f'delta_wij_12 = {delta_wij_12}\n')

        delta_wij_22 = eta * z2 * delta_j2

        # print(f'delta_wij_22 = {delta_wij_22}\n')

        # pretty sure this is the right formula, as we don't seem to to be using the weights in the pervious 2 formulas
        delta_wb2 = eta * b2 * delta_j2

        # print(f'delta_wb2 = {delta_wb2}\n')

        # Update the weights for j2
        wij_12 += delta_wij_12

        # print(f'wij_12 = {wij_12}\n')

        wij_22 += delta_wij_22

        # print(f'wij_22 = {wij_22}\n')

        wb2 += delta_wb2

        # print(f'wb2 = {wb2}\n')

    print('----------------------------------------------')

    print(f'error = {error}\n')
