file = open("demo.txt", "w")
file.write(
    "Lorem ipsum dolor sit amet, consectetur adipisicing elit. \n Dolores voluptatem maxime iusto aperiam a dolore commodi, molestias sapiente reiciendis. \n Minus magni sapiente quidem nihil, suscipit architecto id velit quis voluptatibus.")

file = open("demo.txt", "a")
file.write(
    " \n Lorem ipsum dolor sit amet, consectetur adipisicing elit. \n Autem excepturi labore minima dolor dolores accusantium cum veniam sunt aspernatur perferendis, \n dolorum necessitatibus illum eos tempora reiciendis eius quod in ullam.")

file = open("demo.txt", "r")
print(file.read())

file.close()
