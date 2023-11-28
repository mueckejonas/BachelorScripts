int TreeToHist()
{
  //define folders of Root Tree File and where to write Hist Files
  char rootFile1[] = "/home/jmuecke/code/mueckejonas/BachelorArbeitJM/BachelorStorage/PlotJetKInematics/Root/JetMET0_Run2023B-PromptNanoAODv11p9_v1-v1_NANOAOD.root";
  char rootFile2[] = "/home/jmuecke/code/mueckejonas/BachelorArbeitJM/BachelorStorage/PlotJetKInematics/Root/JetMET1_Run2023B-PromptNanoAODv11p9_v1-v1_NANOAOD.root";
  char outName[] = "/home/jmuecke/code/mueckejonas/BachelorArbeitJM/BachelorStorage/PlotJetKInematics/Root/Hists_Run2023B.root";


   TChain tree("Events");   // name of the tree is the argument
   tree.Add(rootFile1);
   tree.Add(rootFile2);

  //declare variables to Load from Root Tree
  const unsigned int eventNum = 1;
  //variables of Jet1
  float pt1Num[eventNum];
  float y1Num[eventNum];
  float eta1Num[eventNum];
  float phi1Num[eventNum];
  float mass1Num[eventNum];
  float jec1Num[eventNum];
  float muf1Num[eventNum];
  float nhf1Num[eventNum];
  float chf1Num[eventNum];
  float area1Num[eventNum];
  float nemf1Num[eventNum];
  float cemf1Num[eventNum];
  float btagDeepFlavB1Num[eventNum];
  float nConstituents1Num[eventNum];

  tree.SetBranchAddress("jetAK4_pt1",&pt1Num);
  tree.SetBranchAddress("jetAK4_y1",&y1Num);
  tree.SetBranchAddress("jetAK4_eta1",&eta1Num);
  tree.SetBranchAddress("jetAK4_phi1",&phi1Num);
  tree.SetBranchAddress("jetAK4_mass1",&mass1Num);
  tree.SetBranchAddress("jetAK4_jec1",&jec1Num);
  tree.SetBranchAddress("jetAK4_muf1",&muf1Num);
  tree.SetBranchAddress("jetAK4_nhf1",&nhf1Num);
  tree.SetBranchAddress("jetAK4_chf1",&chf1Num);
  tree.SetBranchAddress("jetAK4_area1",&area1Num);
  tree.SetBranchAddress("jetAK4_nemf1",&nemf1Num);
  tree.SetBranchAddress("jetAK4_cemf1",&cemf1Num);
  tree.SetBranchAddress("jetAK4_btagDeepFlavB1",&btagDeepFlavB1Num);
  tree.SetBranchAddress("jetAK4_nConstituents1",&nConstituents1Num);

  //(["pt","y","eta","phi","mass","jec","muf","nhf","chf","area","nemf","cemf","btagDeepFlavB","nConstituents","yboost","chi","mjj"])
  //([[0,4000],[-6,6],[-6,6],[-4,4],[0,500],[0.5,1.5],[0,1],[0,1],[0,1],[0.3,0.6],[0,1],[0,1],[0,1],[0,100],[0,3],[0,20],[0,10000]])

  TH1D pt1("datapt1","pt for jet1 data",50,0,4000);
  pt1.Sumw2();
  TH1D y1("datay1","y for jet1 data",50,-6,6);
  y1.Sumw2();
  TH1D eta1("dataeta1","eta for jet1 data",50,-6,6);
  eta1.Sumw2();
  TH1D phi1("dataphi1","phi for jet1 data",50,-4,4);
  phi1.Sumw2();
  TH1D mass1("datamass1","mass for jet1 data",50,0,500);
  mass1.Sumw2();
  TH1D jec1("datajec1","jec for jet1 data",50,0.5,1);
  jec1.Sumw2();
  TH1D muf1("datamuf1","muf for jet1 data",50,0,1);
  muf1.Sumw2();
  TH1D nhf1("datanhf1","nhf for jet1 data",50,0,1);
  nhf1.Sumw2();
  TH1D chf1("datachf1","chf for jet1 data",50,0,1);
  chf1.Sumw2();
  TH1D area1("dataarea1","area for jet1 data",50,0.3,0.6);
  area1.Sumw2();
  TH1D nemf1("datanemf1","nemf for jet1 data",50,0,1);
  nemf1.Sumw2();
  TH1D cemf1("datacemf1","cemf for jet1 data",50,0,1);
  cemf1.Sumw2();
  TH1D btagDeepFlavB1("databtagDeepFlavB1","btagDeepFlavB for jet1 data",50,0,1);
  btagDeepFlavB1.Sumw2();
  TH1D nConstituents1("datanConstituents1","nConstituents for jet1 data",50,0,100);
  nConstituents1.Sumw2();

  //variables of Jet2
  float pt2Num[eventNum];
  float y2Num[eventNum];
  float eta2Num[eventNum];
  float phi2Num[eventNum];
  float mass2Num[eventNum];
  float jec2Num[eventNum];
  float muf2Num[eventNum];
  float nhf2Num[eventNum];
  float chf2Num[eventNum];
  float area2Num[eventNum];
  float nemf2Num[eventNum];
  float cemf2Num[eventNum];
  float btagDeepFlavB2Num[eventNum];
  float nConstituents2Num[eventNum];

  tree.SetBranchAddress("jetAK4_pt2",&pt2Num);
  tree.SetBranchAddress("jetAK4_y2",&y2Num);
  tree.SetBranchAddress("jetAK4_eta2",&eta2Num);
  tree.SetBranchAddress("jetAK4_phi2",&phi2Num);
  tree.SetBranchAddress("jetAK4_mass2",&mass2Num);
  tree.SetBranchAddress("jetAK4_jec2",&jec2Num);
  tree.SetBranchAddress("jetAK4_muf2",&muf2Num);
  tree.SetBranchAddress("jetAK4_nhf2",&nhf2Num);
  tree.SetBranchAddress("jetAK4_chf2",&chf2Num);
  tree.SetBranchAddress("jetAK4_area2",&area2Num);
  tree.SetBranchAddress("jetAK4_nemf2",&nemf2Num);
  tree.SetBranchAddress("jetAK4_cemf2",&cemf2Num);
  tree.SetBranchAddress("jetAK4_btagDeepFlavB2",&btagDeepFlavB2Num);
  tree.SetBranchAddress("jetAK4_nConstituents2",&nConstituents2Num);

  TH1D pt2("datapt2","pt for jet2 data",50,0,4000);
  pt2.Sumw2();
  TH1D y2("datay2","y for jet2 data",50,-6,6);
  y2.Sumw2();
  TH1D eta2("dataeta2","eta for jet2 data",50,-6,6);
  eta2.Sumw2();
  TH1D phi2("dataphi2","phi for jet2 data",50,-4,4);
  phi2.Sumw2();
  TH1D mass2("datamass2","mass for jet2 data",50,0,500);
  mass2.Sumw2();
  TH1D jec2("datajec2","jec for jet2 data",50,0.5,1);
  jec2.Sumw2();
  TH1D muf2("datamuf2","muf for jet2 data",50,0,1);
  muf2.Sumw2();
  TH1D nhf2("datanhf2","nhf for jet2 data",50,0,1);
  nhf2.Sumw2();
  TH1D chf2("datachf2","chf for jet2 data",50,0,1);
  chf2.Sumw2();
  TH1D area2("dataarea2","area for jet2 data",50,0.3,0.6);
  area2.Sumw2();
  TH1D nemf2("datanemf2","nemf for jet2 data",50,0,1);
  nemf2.Sumw2();
  TH1D cemf2("datacemf2","cemf for jet2 data",50,0,1);
  cemf2.Sumw2();
  TH1D btagDeepFlavB2("databtagDeepFlavB2","btagDeepFlavB for jet2 data",50,0,1);
  btagDeepFlavB2.Sumw2();
  TH1D nConstituents2("datanConstituents2","nConstituents for jet2 data",50,0,100);
  nConstituents2.Sumw2();

  //variables of Jet3
  float pt3Num[eventNum];
  float y3Num[eventNum];
  float eta3Num[eventNum];
  float phi3Num[eventNum];
  float mass3Num[eventNum];
  float jec3Num[eventNum];
  float muf3Num[eventNum];
  float nhf3Num[eventNum];
  float chf3Num[eventNum];
  float area3Num[eventNum];
  float nemf3Num[eventNum];
  float cemf3Num[eventNum];
  float btagDeepFlavB3Num[eventNum];
  float nConstituents3Num[eventNum];

  tree.SetBranchAddress("jetAK4_pt3",&pt3Num);
  tree.SetBranchAddress("jetAK4_y3",&y3Num);
  tree.SetBranchAddress("jetAK4_eta3",&eta3Num);
  tree.SetBranchAddress("jetAK4_phi3",&phi3Num);
  tree.SetBranchAddress("jetAK4_mass3",&mass3Num);
  tree.SetBranchAddress("jetAK4_jec3",&jec3Num);
  tree.SetBranchAddress("jetAK4_muf3",&muf3Num);
  tree.SetBranchAddress("jetAK4_nhf3",&nhf3Num);
  tree.SetBranchAddress("jetAK4_chf3",&chf3Num);
  tree.SetBranchAddress("jetAK4_area3",&area3Num);
  tree.SetBranchAddress("jetAK4_nemf3",&nemf3Num);
  tree.SetBranchAddress("jetAK4_cemf3",&cemf3Num);
  tree.SetBranchAddress("jetAK4_btagDeepFlavB3",&btagDeepFlavB3Num);
  tree.SetBranchAddress("jetAK4_nConstituents3",&nConstituents3Num);

  TH1D pt3("datapt3","pt for jet3 data",50,0,4000);
  pt3.Sumw2();
  TH1D y3("datay3","y for jet3 data",50,-6,6);
  y3.Sumw2();
  TH1D eta3("dataeta3","eta for jet3 data",50,-6,6);
  eta3.Sumw2();
  TH1D phi3("dataphi3","phi for jet3 data",50,-4,4);
  phi3.Sumw2();
  TH1D mass3("datamass3","mass for jet3 data",50,0,500);
  mass3.Sumw2();
  TH1D jec3("datajec3","jec for jet3 data",50,0.5,1);
  jec3.Sumw2();
  TH1D muf3("datamuf3","muf for jet3 data",50,0,1);
  muf3.Sumw2();
  TH1D nhf3("datanhf3","nhf for jet3 data",50,0,1);
  nhf3.Sumw2();
  TH1D chf3("datachf3","chf for jet3 data",50,0,1);
  chf3.Sumw2();
  TH1D area3("dataarea3","area for jet3 data",50,0.3,0.6);
  area3.Sumw2();
  TH1D nemf3("datanemf3","nemf for jet3 data",50,0,1);
  nemf3.Sumw2();
  TH1D cemf3("datacemf3","cemf for jet3 data",50,0,1);
  cemf3.Sumw2();
  TH1D btagDeepFlavB3("databtagDeepFlavB3","btagDeepFlavB for jet3 data",50,0,1);
  btagDeepFlavB3.Sumw2();
  TH1D nConstituents3("datanConstituents3","nConstituents for jet3 data",50,0,100);
  nConstituents3.Sumw2();

  //Create quantities calculated from variables
  TH1D MjjHist("datamjj","Mjj [Gev]",50,0,10000);
  MjjHist.Sumw2();

  TH1D YBoostHist("datayboost","YBoost",50,0,3);
  YBoostHist.Sumw2();

  TH1D ChiHist("datachi","Chi",50,0,20);
  ChiHist.Sumw2();

  //Fill the Hists with Root Tree Data
  for (Long64_t entry = 0; entry < tree.GetEntries(); ++entry)
  {
    tree.GetEntry(entry);
    //Fill Jet1
    pt1.Fill(pt1Num[0]);
    y1.Fill(y1Num[0]);
    eta1.Fill(eta1Num[0]);
    phi1.Fill(phi1Num[0]);
    mass1.Fill(mass1Num[0]);
    jec1.Fill(jec1Num[0]);
    muf1.Fill(muf1Num[0]);
    nhf1.Fill(nhf1Num[0]);
    chf1.Fill(chf1Num[0]);
    area1.Fill(area1Num[0]);
    nemf1.Fill(nemf1Num[0]);
    cemf1.Fill(cemf1Num[0]);
    btagDeepFlavB1.Fill(btagDeepFlavB1Num[0]);
    nConstituents1.Fill(nConstituents1Num[0]);

    //Fill Jet2
    pt2.Fill(pt2Num[0]);
    y2.Fill(y2Num[0]);
    eta2.Fill(eta2Num[0]);
    phi2.Fill(phi2Num[0]);
    mass2.Fill(mass2Num[0]);
    jec2.Fill(jec2Num[0]);
    muf2.Fill(muf2Num[0]);
    nhf2.Fill(nhf2Num[0]);
    chf2.Fill(chf2Num[0]);
    area2.Fill(area2Num[0]);
    nemf2.Fill(nemf2Num[0]);
    cemf2.Fill(cemf2Num[0]);
    btagDeepFlavB2.Fill(btagDeepFlavB2Num[0]);
    nConstituents2.Fill(nConstituents2Num[0]);

    //Fill Jet3
    pt3.Fill(pt3Num[0]);
    y3.Fill(y3Num[0]);
    eta3.Fill(eta3Num[0]);
    phi3.Fill(phi3Num[0]);
    mass3.Fill(mass3Num[0]);
    jec3.Fill(jec3Num[0]);
    muf3.Fill(muf3Num[0]);
    nhf3.Fill(nhf3Num[0]);
    chf3.Fill(chf3Num[0]);
    area3.Fill(area3Num[0]);
    nemf3.Fill(nemf3Num[0]);
    cemf3.Fill(cemf3Num[0]);
    btagDeepFlavB3.Fill(btagDeepFlavB3Num[0]);
    nConstituents3.Fill(nConstituents3Num[0]);

    //Calculate and fill Mjj
    TLorentzVector Lorentz0, Lorentz1;
    Lorentz0.SetPtEtaPhiM(pt1Num[0],eta1Num[0],phi1Num[0],mass1Num[0]);
    Lorentz1.SetPtEtaPhiM(pt2Num[0],eta2Num[0],phi2Num[0],mass2Num[0]);
    TLorentzVector MjjSum = Lorentz0 + Lorentz1;
    double MjjValue = MjjSum.M();
    MjjHist.Fill(MjjValue);

    //Calculate and fill yboost
    double YBoostValue = (y1Num[0]+y2Num[0])/2;
    YBoostHist.Fill(YBoostValue);

    //Calculate and fill chi
    double ChiValue = exp(abs(y1Num[0]-y2Num[0]));
    ChiHist.Fill(ChiValue);
  }

  //Neccesary so files dont get lost
  pt1.SetDirectory(0);
  pt1.SetDirectory(0);
  y1.SetDirectory(0);
  eta1.SetDirectory(0);
  phi1.SetDirectory(0);
  mass1.SetDirectory(0);
  jec1.SetDirectory(0);
  muf1.SetDirectory(0);
  nhf1.SetDirectory(0);
  chf1.SetDirectory(0);
  area1.SetDirectory(0);
  nemf1.SetDirectory(0);
  cemf1.SetDirectory(0);
  btagDeepFlavB1.SetDirectory(0);
  nConstituents1.SetDirectory(0);
  pt2.SetDirectory(0);
  pt2.SetDirectory(0);
  y2.SetDirectory(0);
  eta2.SetDirectory(0);
  phi2.SetDirectory(0);
  mass2.SetDirectory(0);
  jec2.SetDirectory(0);
  muf2.SetDirectory(0);
  nhf2.SetDirectory(0);
  chf2.SetDirectory(0);
  area2.SetDirectory(0);
  nemf2.SetDirectory(0);
  cemf2.SetDirectory(0);
  btagDeepFlavB2.SetDirectory(0);
  nConstituents2.SetDirectory(0);
  pt3.SetDirectory(0);
  pt3.SetDirectory(0);
  y3.SetDirectory(0);
  eta3.SetDirectory(0);
  phi3.SetDirectory(0);
  mass3.SetDirectory(0);
  jec3.SetDirectory(0);
  muf3.SetDirectory(0);
  nhf3.SetDirectory(0);
  chf3.SetDirectory(0);
  area3.SetDirectory(0);
  nemf3.SetDirectory(0);
  cemf3.SetDirectory(0);
  btagDeepFlavB3.SetDirectory(0);
  nConstituents3.SetDirectory(0);
  MjjHist.SetDirectory(0);
  YBoostHist.SetDirectory(0);
  ChiHist.SetDirectory(0);

  TFile* outHistFile = TFile::Open(outName,"RECREATE");
  //Write Jet1 Data to Root
  outHistFile->mkdir("Jet1Data");
  outHistFile->cd("Jet1Data");
  pt1.Write();
  y1.Write();
  eta1.Write();
  phi1.Write();
  mass1.Write();
  jec1.Write();
  muf1.Write();
  nhf1.Write();
  chf1.Write();
  area1.Write();
  nemf1.Write();
  cemf1.Write();
  btagDeepFlavB1.Write();
  nConstituents1.Write();
  //Write Jet2 Data to Root
  outHistFile->mkdir("Jet2Data");
  outHistFile->cd("Jet2Data");
  pt2.Write();
  y2.Write();
  eta2.Write();
  phi2.Write();
  mass2.Write();
  jec2.Write();
  muf2.Write();
  nhf2.Write();
  chf2.Write();
  area2.Write();
  nemf2.Write();
  cemf2.Write();
  btagDeepFlavB2.Write();
  nConstituents2.Write();
  //Write Jet3 Data to Root
  outHistFile->mkdir("Jet3Data");
  outHistFile->cd("Jet3Data");
  pt3.Write();
  y3.Write();
  eta3.Write();
  phi3.Write();
  mass3.Write();
  jec3.Write();
  muf3.Write();
  nhf3.Write();
  chf3.Write();
  area3.Write();
  nemf3.Write();
  cemf3.Write();
  btagDeepFlavB3.Write();
  nConstituents3.Write();
  //Write quantities to Root
  outHistFile->mkdir("Kinematics");
  outHistFile->cd("Kinematics");
  MjjHist.Write();
  YBoostHist.Write();
  ChiHist.Write();
  outHistFile->Close();
  return 0;
}
