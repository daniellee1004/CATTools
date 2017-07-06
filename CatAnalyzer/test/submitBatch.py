#!/usr/bin/env python 
# catGetDatasetInfo v7-4-4 # to make dataset lists
# sed -i 's/^\/store/root:\/\/cms-xrdr.sdfarm.kr:1094\/\/xrd\/store/g' *

import os
username = os.environ['USER']

analysis = 'h2muAnalyzer'
#analysis = 'TtbarDiLeptonAnalyzer'

pythonCfg = 'run_'+analysis+'_cfg.py'
#analysis=analysis+'Silver'

import os,json
datadir = os.environ["CMSSW_BASE"]+'/src/CATTools/CatAnalyzer/data/dataset/'
dataset_json = datadir + 'dataset.json'
version = os.environ["CMSSW_VERSION"]

with open(dataset_json) as data_file:    
    data = json.load(data_file)
    for i in data:
        #print data[0]
        datasetName = i['name']
        if "QCD" in datasetName:
            continue
        if "Electron" in datasetName:
            continue       
        if "Photon" in datasetName:
            continue 
        if "QCD" in datasetName:
            continue
        if "Top" in datasetName:
            continue 
        if "powheg" in datasetName:
            continue
        if "Double" in datasetName:
            continue 
        if "ttZ" in datasetName:
            continue
        if "ttW" in datasetName:
            continue

        fileList = datadir + 'dataset_' + datasetName + '.txt'
        jobName = analysis+'_'+datasetName
        #createbatch = "create-batch --cfg %s --jobName %s --fileList %s --maxFiles 10"%(pythonCfg, jobName, fileList) 
        #createbatch = "create-batch --cfg %s --jobName %s --fileList %s --maxFiles 50 --transferDest \"root://cms-xrdr.sdfarm.kr:1094//xrd/store/user/pseudotop/ntuples/%s/%s\""%(pythonCfg, jobName, fileList, version, datasetName)
        createbatch = "create-batch --cfg %s --jobName %s --fileList %s --maxFiles 50 --transferDest \"root://cms-xrdr.sdfarm.kr:1094//xrd/store/user/%s/cattree/%s/%s\""%(pythonCfg, jobName, fileList, username, version, datasetName)
        print createbatch
        os.system(createbatch)
        
