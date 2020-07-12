import json
import argparse
from random import randrange


parser = argparse.ArgumentParser()
parser.add_argument('filenames', type=argparse.FileType(), nargs='+',help='add files names')
parser.add_argument('-o','--output',type=str,help='output filename')
args = parser.parse_args()
# filelist=args.filenames
output=args.output

def getfilelist():
    listoffiles=list()
    for file in args.filenames:
        listoffiles.append(file.name)
    return listoffiles


def getmergedstatement(filelist):
    statementList=list()
    for f in range(len(filelist)):
        f=json.loads(open(filelist[f],"r").read())
        statement=f["Statement"][0]
        statement["Sid"]=f["Statement"][0]["Sid"]+"-"+str(randrange(1000))
        statementList.append(statement)
    return statementList

filelist=getfilelist()
print(filelist)

def getmergedstatement(filelist):
    statementList=list()
    for f in range(len(filelist)):
        f=json.loads(open(filelist[f],"r").read())
        statement=f["Statement"][0]
        statement["Sid"]=f["Statement"][0]["Sid"]+"-"+str(randrange(1000))
        statementList.append(statement)
    return statementList
    
def getNewMergedPolicy():
    if len(filelist)>0:
        policy={
            "Version": "2008-10-17",
            "Id": "__default_policy_haha_ID",
            "Statement": getmergedstatement(filelist)
        }
        with open(output,"w") as pf:
            pf.write(json.dumps(policy,indent=2, sort_keys=True))
            pf.close()
    else:
        print("we filelist is empty")
        

if __name__ == "__main__":
    getNewMergedPolicy()
