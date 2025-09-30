if __name__ == '__main__':

    try:
        with open('example_txt1.py', 'r') as file:
            print(file.readline())
    
    except Exception as e:
        print(e)
        