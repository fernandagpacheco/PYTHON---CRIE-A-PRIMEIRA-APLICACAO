import os

movies = [
    {"title" : "Kill Bill - Vol I", "year" : "2003", "seen" :False},
    {"title" : "Inglourious Basterds", "year" : "2009", "seen" :False},
    {"title" : "Pulp Fiction", "year" : "1994", "seen" :True}
    ]

def app_name():
    print("""
🔪🔪🔪🔪🔪🔪🔪🔪🔪🔪🔪🔪🔪🔪🔪🔪🔪🔪🔪🔪😵
                    
ᵀᵃʳᵃⁿᵗⁱⁿᵒ'ˢ ᴿᵉᵉˡ ᴰᵉᵃˡ⠘ ᴬ ᴾʸᵗʰᵒⁿ ᶠˡⁱᶜᵏ ᴸⁱˢᵗ
          
💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥🔫           
          """)

def view_options():
    print("1.Add movie")
    print("2.List movies")
    print("3.Upload movie")
    print("4.Exit\n")

def end_app():
    display_text("This app's going out like a bloody shootout in my movies - time to wrap it up!")

def main_menu():
    input("\nHit a damn key to get back")
    main()

def invalid_option():
    print("That option ain't worth a shot in my script - pick something else!\n")
    main_menu()

def display_text(text):
    """
    Clear the screen and displays the given text with a decorative emoji border.

    Parameters: 
    text(str): The text to display inside the visual frame.
    """
    os.system("cls")
    line = "🔥***************💣****************💥💥💥💥💥💥😵\n" 
    anotherline = "\n😵💥💥💥💥💥💥****************💣***************🔥"
    print(line)
    print(text)
    print(anotherline)
    print()


def adding_movie():
    """
    Prompts the user to input a movie title and release year. Adds the movie to the movies list and returns to the main menu.

    The movie is stored as a dictionary with title, year, and seen status (default: False).
    """
    display_text("Adding another one")
    movie_title = input("Type the damn movie title: ")
    year = input("Punch in the movie's year:")
    movie_info = {"title": movie_title, "year": year, "seen": False}
    movies.append(movie_info)
    print(f"\n {movie_title} is been locked into the list")

    main_menu()

def list_movies():
    display_text("Here's the killer lineup of favorites")

    print(f"{"Movie's title".ljust(22)} | {"Year".ljust(20)} | Status\n")

    for movie in movies:
        title = movie["title"]
        year = movie["year"]
        active = "Seen" if movie["seen"] else "Not seen"
        print(f"- {title.ljust(20)} | {year.ljust(20)} | {active}")

    main_menu()

def upload():
    display_text("Tagging as seen")
    movie_title = input("Type the movie title to mark it as seen: ")
    movie_found = False

    for movie in movies:
        if movie_title == movie["title"]:
            movie_found = True
            movie["seen"] = not movie["seen"]
            message = f"\n {movie_title} was uploaded" if movie["seen"] else f"\n{movie_title} was not uploaded"
            print(message)

    if not movie_found:
        print("Are you drunk? There's no such a thing")

    main_menu()




def pick_an_option():

    try:

        pick_option = int(input("\nPick a damn option, or I'll write a script where you're stuck in a loop forever!\n"))

        if pick_option == 1:
            adding_movie()
        elif pick_option == 2:
            list_movies()
        elif pick_option == 3:
            upload()
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




