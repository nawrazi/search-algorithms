import matplotlib.pyplot as plt



def plot_graph(solution):
    
    item_list = list()
    item_value = list()

    for item in solution:
        item_list.append(item)
        item_value.append(solution[item])

    print(item_list)
    print(item_value)

    plt.bar(item_list, item_value, color = "brown")
    plt.xlabel("items")
    plt.ylabel("value ")
    plt.title('knapsack with Hill Climbing')
    plt.show()