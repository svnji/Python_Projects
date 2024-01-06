def main () :
    Lang = input("Arabic or English? : ")
    if Lang.lower() == ("english"):
        def sayhi(name, age):
            print("Hello " + name)
            Gen = input("Male or Female : ")
            if Gen.lower() == ("male"):
                print("Your name is : " + name)
                print("Your age is : " + age )
                print("Your Gander is : " + Gen )
            elif Gen.lower() == ("female"):
                print("Your name is : " + name)
                print("Your age is : " + age)
                print("Your Gander is : " + Gen)
            else:
                print("Error")
            answer = input("That's right ? : ")
            if answer.lower() == "no" :
                main()
            elif answer.lower() == "nope" :
                main()
            else:
                print("Yeaah 3> ")
                print("Thanks for trying :D,Have a good day 3>")
                again = input("Exit (Yes or No) ? ")
                if again.lower() == "no":
                    main()

        sayhi(input("Enter Your Name : "), input("enter ur age : "))
    elif Lang.lower() == ("eng"):
        def sayhi(name, age):
            print("Hello " + name)
            Gen = input("Male or Female : ")
            if Gen.lower() == ("male"):
                print("Your name is : " + name)
                print("Your age is : " + age)
                print("Your Gander is : " + Gen)
            elif Gen.lower() == "female":
                print("Your name is : " + name)
                print("Your age is : " + age)
                print("Your Gander is : " + Gen)
            else:
                print("Error")
            answer = input("That's right ? : ")
            if answer.lower() == "no":
                main()
            elif answer.lower() == "nope":
                main()
            else:
                print("Yeaah 3> ")
                print("Thanks for trying :D,Have a good day 3>")
                again = input("Exit (Yes or No) ? ")
                if again.lower() == "no":
                    main()

        sayhi(input("Enter Your Name : "), input("enter ur age : "))
    elif Lang.lower() == ("arabic"):
        def sayhi2(name, age):
            print("مرحبا " + name)
            Gen = input("ذكر أو انثى : ")
            if Gen.lower() == ("ذكر"):
                print("انت ذكر و لديك " + age + " عاما !")
            elif Gen.lower() == ("رجل"):
                print("انت ذكر و لديك " + age + " عاما !")
            elif Gen.lower() == ("انثي"):
                print("انت انثى ولديكي " + age + " عاما !")
            elif Gen.lower() == ("انثى"):
                print("انت انثى ولديكي " + age + " عاما !")
            else:
                print("Error")
            answer = input("هل كان هذا صحيحا ؟ : ")
            if answer.lower() == "لاء":
                main()
            elif answer.lower() == "لا":
                main()
            else:
                print("مرحا 3> ")
                print("Thanks for trying :D,Have a good day 3>")
                again = input("Exit (Yes or No) ? ")
                if again.lower() == "no":
                    main()

        sayhi2(input("ادخل اسمك : "), input("ادخل عمرك : "))
    elif Lang.lower() == ("ar"):
        def sayhi2(name, age):
            print("مرحبا " + name)
            Gen = input("ذكر أو انثى : ")
            if Gen.lower() == ("ذكر"):
                print("انت ذكر و لديك " + age + " عاما !")
            elif Gen.lower() == ("رجل"):
                print("انت ذكر و لديك " + age + " عاما !")
            elif Gen.lower() == ("انثي"):
                print("انت انثى ولديكي " + age + " عاما !")
            elif Gen.lower() == ("انثى"):
                print("انت انثى ولديكي " + age + " عاما !")
            else:
                print("Error")
            answer = input("هل كان هذا صحيحا ؟ : ")
            if answer.lower() == "لاء":
                main()
            elif answer.lower() == "لا":
                main()
            else:
                print("مرحا 3> ")
                print("Thanks for trying :D,Have a good day 3>")
                again = input("Exit (Yes or No) ? ")
                if again.lower() == "no":
                    main()

        sayhi2(input("ادخل اسمك : "), input("ادخل عمرك : "))
    else:
        print("error")

main()

print("Thanks for trying :D,Have a good day 3>")
again = input("Exit (Yes or No) ? ")
if again.lower()=="no":
    main()
