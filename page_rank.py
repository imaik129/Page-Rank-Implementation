
"""all_pages represents our adjacency list implementation. The damping factor is also defined here. """
all_pages = []
damping_factor = 0.85

"""page object that keeps track of the name, page_rank, previous_page_rank,
and the children of each page.  """
class page:
    def __init__(self, page_name, page_rank,prev_page_rank):
        self.page_name = page_name
        self.children= []
        self.parents=[]
        self.page_rank= page_rank
        self.prev_page_rank = prev_page_rank

"""Param: text-file to be parsed. Method to convert an appropriately formatted text file into a directed graph"""
def convert_text_to_graph(text_file):
    """parse txt file"""
    with open(text_file) as file:
        rows = file.readlines()
        first_line = rows[1]

    first_line = first_line.split(",")

    for node in first_line:
        node = node.strip('\n')
        new_page = page(node, 0, 0)
        all_pages.append(new_page)

    """create edges"""
    for row in rows[2:]:
        edge = row.split(",")
        source = edge[0]
        target = edge[1]

        """clean up string"""
        source = source.strip('\n')
        target = target.strip('\n')

        for i in all_pages:
            if i.page_name == source:
                for j in all_pages:
                    if j.page_name == target:
                        (i.children).append(j)
                        (j.parents).append(i)

""" Method to calculate the new_page_rank given the total page number,
number of links, current page rank,   """
def new_page_rank(prev_page_rank, num_of_links, bool):
    if bool:
        new_page_rank = damping_factor * (prev_page_rank/num_of_links)
    else:
        total_page_num = len(all_pages)
        new_page_rank = damping_factor * (prev_page_rank/total_page_num)
    return new_page_rank

"""calculate the appropriate page rank for each page"""
def find_page_rank():
    all_pages_num = len(all_pages)

    for node in all_pages:
        temp = 0
        if len(node.parents) != 0:
            for adj_node in node.parents:
                num_of_children = len(adj_node.children)

                temp = temp + (damping_factor * (adj_node.page_rank/num_of_children))

                print("LENGTH: ", len(adj_node.children))
                print(adj_node.page_name)
                for i in adj_node.children:
                    print(i.page_name)

                if len(adj_node.children) == 0:
                    print("in this case")
                    temp = temp + (damping_factor * node.page_rank/all_pages_num)
        else:
            temp = node.page_rank

        node.prev_page_rank = node.page_rank
        node.page_rank = (1-damping_factor)/all_pages_num + temp

"""method to print each page and its relevant information"""
def print_graph():
    for element in all_pages:
        print("name: ", element.page_name)
        print("children: ")
        for i in element.children:
            print(i.page_name)
        print("parents: ")
        for j in element.parents:
            print(j.page_name)
        print("page_rank: ", element.page_rank)


"""method to check if there was a change of more than x
for any of the pageranks by comparing. Returns boolean"""
def check_difference(x):
    for node in all_pages:
        # print(abs(node.prev_page_rank-node.page_rank))
        if x > abs(node.prev_page_rank - node.page_rank):
            return False
    return True

"""Method to intialize the page ranks and run the algorithm as long as the difference is
greater than a certain input value"""
def run_page_rank(x):
    #initialize
    all_pages_num = len(all_pages)

    for node in all_pages:
        node.page_rank = 1/all_pages_num
    counter = 0

    while(check_difference(x)==True):
        counter += 1
        find_page_rank()
    return counter

"""method for running page rank a certain number of iterations"""
# def run_page_rank(num_of_iteration):
#     #initialize
#     all_pages_num = len(all_pages)
#     for node in all_pages:
#         node.page_rank = 1/all_pages_num
#     for i in range(num_of_iteration):
#         find_page_rank()

"""method to return formatted string of page ranks"""
def return_formatted_page_rank(num_of_iterations):
    print("The program iterated: ", num_of_iterations, " times.")
    for one_page in all_pages:
        print(one_page.page_name, ": ", one_page.page_rank)

"""main method"""
def main():
    """change parameter to change test case"""
    convert_text_to_graph('test1.txt')
    """change parameter to change damping factor"""
    num_of_iterations = run_page_rank(0.0001)
    return_formatted_page_rank(num_of_iterations)
    print_graph()


if __name__ == "__main__":
    main()
