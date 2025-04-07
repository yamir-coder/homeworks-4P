def main():
    print("(English): The more difficult the victory, the greater the happiness in winning.")

    while True:
        print("\nChoose a language to translate the quote:")
        print("1. Spanish")
        print("2. French")
        print("3. German")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            print("Spanish: Cuanto más difícil es la victoria, mayor es la felicidad de ganar.")
        elif choice == "2":
            print("French: Plus la victoire est difficile, plus le bonheur de gagner est grand.")
        elif choice == "3":
            print("German: Je schwieriger der Sieg, desto größer die Freude über den Sieg.")
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
