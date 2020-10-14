def game():
    my_hp = 1000
    my_power = 200
    your_hp = 1000
    your_power = 199
    my_final_hp = my_hp - your_power
    enemy_hp = your_hp - my_power

    print("You Win") if my_final_hp > enemy_hp else print("You lose")
    while True:
        my_hp = my_final_hp - your_power
        your_hp = your_hp - my_power
        if my_hp <= 0:
            print("You win")
            break
        elif your_hp <= 0:
            print("You lose")
            break


game()
