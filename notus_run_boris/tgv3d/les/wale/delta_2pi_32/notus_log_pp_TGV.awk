BEGIN {
        time=0
        MeanKE=0
        MeanP=0
        MeanKEDR=0
        }{
  if (NF > 1) {
    if (($1 == "Time")    && ($2 == "iteration")) {                           time=$9
                                                                          #ite=$4
                                               }
    if (($1 == "Mean") && ($2 == "kinetic") && ($3 == "energy:")) {        MeanKE=$4}
    if (($1 == "Mean") && ($2 == "pressure:")) {        MeanP=$3}
    if (($1 == "Mean") && ($2 == "kinetic") && ($3 == "energy") && ($4 == "dissipation")) {        MeanKEDR=$6
  print time, MeanKE, MeanKEDR, MeanP
    }
  }
}

