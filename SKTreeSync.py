import os 
from os import listdir
from os.path import isfile,isdir, join


#eras=["2016" "2016preVFP","2016postVFP","2017","2018"]
eras = ["2016preVFP","2016postVFP","2017","2018"]  

for era in eras:

    mc_path="/pnfs/knu.ac.kr/data/cms/store/user/jalmond/SKFlat/"+era+"/"    
    
    if not os.path.exists(mc_path):
        continue

    DSList = [f for f in listdir(mc_path) if isdir(join(mc_path,f))]

    for DSN in DSList:

        tamsa_path= '/gv0/DATA/SKFlat/Run2UltraLegacy_v2/'

        prod_path=mc_path+DSN+"/SKFlat_Run2UltraLegacy_v2/"

        if os.path.exists(prod_path):
            ProdTagList = [f for f in listdir(prod_path) if isdir(join(prod_path,f))]

            for prod in ProdTagList:
                print prod_path+prod
            
                print 'rsync -av -e "ssh -p 1240"  /pnfs/knu.ac.kr/data/cms/store/user/jalmond/SKFlat/'+era+'/'+DSN+'/SKFlat_Run2UltraLegacy_v2/'+prod+'  jalmond@147.47.242.42:'+tamsa_path+era+'/MC/'+DSN
                os.system('rsync -av -e "ssh -p 1240"  /pnfs/knu.ac.kr/data/cms/store/user/jalmond/SKFlat/'+era+'/'+DSN+'/SKFlat_Run2UltraLegacy_v2/'+prod+'  jalmond@147.47.242.42:'+tamsa_path + era+'/MC/'+DSN)

        else:

            if "VFP" in era:
                continue
            leg_era=era

            prod_path=mc_path+DSN+"/SKFlat_Run2Legacy_v4/"
            tamsa_path='/gv0/Users/jalmond/SKFlat_Run2Legacy_v4/'

            if os.path.exists(prod_path):
                ProdTagList = [f for f in listdir(prod_path) if isdir(join(prod_path,f))]

                for prod in ProdTagList:
                    print prod_path+prod
                    
                    print 'rsync -av -e "ssh -p 1240"  /pnfs/knu.ac.kr/data/cms/store/user/jalmond/SKFlat/'+era+'/'+DSN+'/SKFlat_Run2Legacy_v4/'+prod+'  jalmond@147.47.242.42:'+tamsa_path+leg_era+'/MC/'+DSN
                    os.system('rsync -av -e "ssh -p 1240"  /pnfs/knu.ac.kr/data/cms/store/user/jalmond/SKFlat/'+era+'/'+DSN+'/SKFlat_Run2Legacy_v4/'+prod+'  jalmond@147.47.242.42:'+tamsa_path + leg_era+'/MC/'+DSN)
