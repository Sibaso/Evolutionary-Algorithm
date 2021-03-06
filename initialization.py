import numpy as np
import math
import data_reader as dp
from data_reader import Edge,read_idpc
POPULATION_SIZE  = 100
NUMBER_OF_PARENTS = 0

INIT_POP = []
class Member:

    edge_prio = []
    out_edge_index = []
    def __init__(self, prio: list, out_edge):

        return

class Egde_IDPC(object):
	def __init__(self,u, v, w, d): # edgu (u, v), weight = w, domain = d
		super(Egde_IDPC, self).__init__()
		self.u = u
		self.v = v
		self.w = w
		self.d = d
		self.pheromone = 0
		self.ants = []
		#self.color = COLORS[d]

	def update_pheromone(self, pheromone_evaporation):
		self.pheromone = (1-pheromone_evaporation)*self.pheromone
		for ant in self.ants:
			self.pheromone += pheromone_const*ant.tour_complete
		self.ants = []
	def print(self):
		print('({}->{}), color: {}, cost: {}'.format(self.u, self.v, self.d, self.w))


class Path:
    def __init__(self):

        return

def weight_prepocessing_func(input_value, log_stenght):
    output_value  = 1/log_stenght*math.log(input_value)
    return output_value

def encoding(path : list,list_edge):
    code = []


    return  code

def roulette_wheel(at_node : Edge,at_domain, list_edge ):
    candidate = [[i,weight_prepocessing_func(at_node.domain_dict[at_domain][i],3)] for i in at_node.domain_dict[at_domain]]
    candidate_node = []
    candidate_weight = []
    for i in range(len(candidate)):
        candidate_node.append(candidate[i][0])
        candidate_weight.append(candidate[i][1])

    tong = sum(candidate_weight)
    candidate_weight = [float(i)/tong for i in candidate_weight]
    next_node = np.random.choice(a=candidate_node,p=candidate_weight)
    return next_node
def choose_path(list_edge ,start_node , terminal_node ,number_of_domain, number_of_node):
    done_signal = True
    domain_passed = []
    path = [[start_node,0]]
    start = start_node
    next_node = start
    path_concak = []
    while(start != terminal_node ):
        now_at_node = list_edge[start]
        candidate_domain = []
        for domain in now_at_node.out_going_domain:
            if(domain not in domain_passed):
                candidate_domain.append(domain)
        if(len(candidate_domain) == 0):
            return [1],[1], False
        else:
            the_chosen_one_domain = np.random.choice(a= candidate_domain)
            the_chosen_one_next_node =  roulette_wheel(now_at_node,the_chosen_one_domain,list_edge)

            next_des = [the_chosen_one_next_node,the_chosen_one_domain]
            domain_passed.append(the_chosen_one_domain)
            edge = Egde_IDPC(start,the_chosen_one_next_node,list_edge[start].domain_dict[the_chosen_one_domain][the_chosen_one_next_node],the_chosen_one_domain)
            start = the_chosen_one_next_node
            path.append(next_des)

            path_concak.append(edge)

    return path_concak,path, done_signal




def pop_init(size_gen,file_name):   #size_gen: s??? l?????ng ph???n t??? d??ng kh???i t???o ????? xu???t, file_name : t??n file.
    NUMBER_OF_NODE, NUMBER_OF_DOMAIN, SOURCE_NODE, TERMINAL_NODE, LIST_EDGE = read_idpc(file_name)
    #Danh s??ch c??c c???nh l??u ??? LIST_EDGE
    #1  ph???n t??? c???a LIST_EDGE l?? con c???a class Edge trong data_reader.
    # 1 Edge c?? domain dict : l??u c??c out-going domain v?? out-going edge n???m b??n trong domain
    # v?? d??? 1 th??nh ph???n con c???a LIST_EDGE:
    #print("hello motherfcker -edge said " )
    #print(LIST_EDGE[0].domain_dict)
    INIT_POP = []
    if(1):
        count = 0
        paths = []
        while(count < size_gen):
            path_concak,path, done_signal = choose_path(LIST_EDGE,SOURCE_NODE,TERMINAL_NODE,NUMBER_OF_DOMAIN,NUMBER_OF_NODE)
            path.append(path_concak)
            if(done_signal == True):
                print("path t??m ???????c ??? ????y:")
                for edge in path_concak:
                    edge.print()
                 # path t??m d?????c ??? ????y, th??ng  Qu??n ch?? ??.
              #  print(path_concak[0].u, path_concak[0].v, path_concak[0].w, path_concak[0].d)
                #path la 1 list l??u th??? t??? c??c [node, domain ????? ??i ?????n node ????y].
                #1 ph???n t??? c???a path  c?? c???u tr??c l?? : [node,domain]: ph???n t??? d???u ti??n l?? th??? t??? node, ph???n t??? th??? 2 l?? domain.
                #t ch??a encoding path, m encoding ki???u g?? th?? nh??t path c???a t v??o r???i encoding
                #INIT_POP l?? danh s??ch c??c encoding


                code = encoding(path, LIST_EDGE)
                INIT_POP.append(code)
                count+=1
            else:
                continue



    return INIT_POP,paths
