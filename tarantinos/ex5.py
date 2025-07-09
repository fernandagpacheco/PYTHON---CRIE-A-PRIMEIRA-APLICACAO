import os

movies = ["Kill Bill - Vol I", "Kill Bill - Vol II"]

def app_name():
    print("""
ᵀᵃʳᵃⁿᵗⁱⁿᵒ'ˢ ᴿᵉᵉˡ ᴰᵉᵃˡ⠘ ᴬ ᴾʸᵗʰᵒⁿ ᶠˡⁱᶜᵏ ᴸⁱˢᵗ
          """)

def view_options():
    print("1.Add movie")
    print("2.List movies")
    print("3.Upload movie")
    print("4.Exit")

def end_app():
    display_text("This app's goin out like a bloody shootout in my movies - time to wrap it up!")

def main_menu():
    input("\nHit a damn key to get back")
    main()

def invalid_option():
    print("That option ain't worth a shot in my script - pick something else!\n")
    main_menu()

def display_text(text):
    os.system("cls")
    print(text)
    print()


def adding_movie():
    display_text("Adding another one")
    movie_title = input("Type the damn movie title: ")
    movies.append(movie_title)
    print(f" {movie_title} is been locked into the list")

    main_menu()

def list_movies():
    display_text("Here's the killer lineup of favorites")

    for movie in movies:
        print(f"- {movie}")

    main_menu()


def pick_an_option():

    try:

        pick_option = int(input("\nPick a damn option, or I'll write a script where you're stuck in a loop forever!\n"))

        if pick_option == 1:
            adding_movie()
        elif pick_option == 2:
            list_movies()
        elif pick_option == 3:
            print("Upload")
        elif pick_option == 4:
            end_app()
        else:
            invalid_option() 
    
    except:
        invalid_option()

def main():
    os.system("cls")
    app_name()
    view_options()
    pick_an_option()

if __name__ == "__main__":
    main()




