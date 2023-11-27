import ROOT
import numpy as np

import ROOT
import numpy as np
#takes three hists and turn them into pdf
def RootHisttoPdf(outFileName,data,simulation,logyScale,yAxisTitle,xAxisTitle,title):
    canvas = ROOT.TCanvas("canvas")
    if logyScale:
        canvas.SetLogy(True)
    canvas.cd()

    latex = ROOT.TLatex()
    latex.SetNDC()
    latex.SetTextSize(0.03)

    legend = ROOT.TLegend(0.7,0.6,0.85,0.75)
    legend.SetLineWidth(0)
    legend.AddEntry(data,"data")
    legend.AddEntry(simulation,"simulation")

    data.SetStats(0)
    data.SetLineColor(ROOT.kBlack)
    data.SetLineWidth(2)
    simulation.SetStats(0)
    simulation.SetLineColor(ROOT.kRed)
    simulation.SetLineWidth(2)
    simulation.SetTitle("")
    data.GetYaxis().SetTitle(yAxisTitle)
    data.GetXaxis().SetTitle(xAxisTitle)
    data.SetTitle("")
    simulation.Scale()
    data.Draw("pe")
    simulation.Draw("h,same")
    legend.Draw("same")
    latex.DrawText(0.7,0.8,title)
    canvas.Print(outFileName)

#define directories
dataInDirectory = "/home/jmuecke/code/mueckejonas/BachelorArbeitJM/BachelorStorage/DijetEventSelection/ROOT/"
simInDirectory = "/home/jmuecke/code/mueckejonas/BachelorArbeitJM/BachelorStorage/PlotSimulation/ROOT/"
outDirectory = "/home/jmuecke/code/mueckejonas/BachelorArbeitJM/BachelorStorage/PlotSimulation/PDF/Together/"
dataInFileName = dataInDirectory+"Hists_Run2023B.root"
simInFileName = simInDirectory+"Run32023_MC.root"

#Get data Jets and Kinematics
dataHistFile = ROOT.TFile.Open(dataInFileName,"READ")
dataJet1 = dataHistFile.Get("Jet1Data")
dataJet2 = dataHistFile.Get("Jet2Data")
dataJet3 = dataHistFile.Get("Jet3Data")
dataKinematics = dataHistFile.Get("Kinematics")

#Get Sim Jets and kinematics
simHistFile = ROOT.TFile.Open(simInFileName,"READ")
simJet1 = simHistFile.Get("Jet1MC")
simJet2 = simHistFile.Get("Jet2MC")
simJet3 = simHistFile.Get("Jet3MC")
simKinematics = simHistFile.Get("MCKinematics")

#define variables to compare and plot as array
JetNameArray = np.array(["pt","y","eta","phi","mass","jec","muf","nhf","chf","area","nemf","cemf","btagDeepFlavB","nConstituents"])
XaxisArray = np.array(["Pt [GeV]","Y","Eta","Phi","Mass [Gev]","Jec","Muf","Nhf","Chf","Area","Nemf","Cemf","BtagDeepFlavB","NConstituents"])

#create data and simulation ratio plots pdfs
for i in range(0,14):
    #get data
    data1 = dataJet1.Get("data"+JetNameArray[i]+"1")
    data2 = dataJet2.Get("data"+JetNameArray[i]+"2")
    data3 = dataJet3.Get("data"+JetNameArray[i]+"3")

    #get simulation
    sim1 = simJet1.Get("MC"+JetNameArray[i]+"1")
    sim2 = simJet2.Get("MC"+JetNameArray[i]+"2")
    sim3 = simJet3.Get("MC"+JetNameArray[i]+"3")

    #create and save pdf files
    if JetNameArray[i] == "pt" or JetNameArray[i] == "mass":
        RootHisttoPdf(outDirectory+JetNameArray[i]+"1DataandSim.pdf",data1,sim1,True,"N",XaxisArray[i],"Data and Simulation for"+JetNameArray[i]+"1")
        RootHisttoPdf(outDirectory+JetNameArray[i]+"2DataandSim.pdf",data2,sim2,True,"N",XaxisArray[i],"Data and Simulation for"+JetNameArray[i]+"2")
        RootHisttoPdf(outDirectory+JetNameArray[i]+"3DataandSim.pdf",data3,sim3,True,"N",XaxisArray[i],"Data and Simulation for"+JetNameArray[i]+"3")
    else:
        RootHisttoPdf(outDirectory+JetNameArray[i]+"1DataandSim.pdf",data1,sim1,False,"N",XaxisArray[i],"Data and Simulation for"+JetNameArray[i]+"1")
        RootHisttoPdf(outDirectory+JetNameArray[i]+"2DataandSim.pdf",data2,sim2,False,"N",XaxisArray[i],"Data and Simulation for"+JetNameArray[i]+"2")
        RootHisttoPdf(outDirectory+JetNameArray[i]+"3DataandSim.pdf",data3,sim3,False,"N",XaxisArray[i],"Data and Simulation for"+JetNameArray[i]+"3")

#create yboost pdf
datayboost = dataKinematics.Get("datayboost")
simyboost = simKinematics.Get("MCyboost")
RootHisttoPdf(outDirectory+"yboostDataandSim.pdf",datayboost,simyboost,False,"N","Yboost","Data and Simulation for Yboost")
#create chi pdf
datachi = dataKinematics.Get("datachi")
simchi = simKinematics.Get("MCchi")
RootHisttoPdf(outDirectory+"chiDataandSim.pdf",datachi,simchi,False,"N","Chi","Data and Simulation for Chi")
#create mjj pdf
datamjj = dataKinematics.Get("datamjj")
simmjj = simKinematics.Get("MCmjj")
RootHisttoPdf(outDirectory+"mjjDataandSim.pdf",datamjj,simmjj,True,"N","Mjj [GeV]","Data and Simulation for Mjj")
