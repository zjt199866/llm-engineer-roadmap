import argparse

def main():

    parser = argparse.ArgumentParser(description="LLM engineer roadmap CLI")
    parser.add_argument("--name",type=str,default="世界",help="要问候的名字")

    parser.add_argument("--repeat",type=int,default=1,help="问候的次数")
    args = parser.parse_args()

    for i in range(args.repeat):
        print(f"你好,{args.name}!")

if __name__ =="__main__":     
    main()
