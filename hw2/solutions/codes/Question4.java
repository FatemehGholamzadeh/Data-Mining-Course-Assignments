package ir.aut;

import weka.associations.AssociationRule;
import weka.associations.AssociationRules;
import weka.associations.BinaryItem;
import weka.associations.FPGrowth;
import weka.core.Instances;
import weka.core.converters.ConverterUtils.DataSource;

import java.util.*;


public class Question4 {

    public static void main(String args[]) throws Exception {

        //defining minimum support
        double sup_min = 0.1;

        //defining number of rules
        int number_of_rules = 10000000;

        ArrayList<Collection<BinaryItem>> Max_pattern = new ArrayList<Collection<BinaryItem>>();

        ArrayList<Collection<BinaryItem>> closed_pattern = new ArrayList<Collection<BinaryItem>>();

        //address of the dataset file
        String dataset = "supermarket.arff";

        //creating an object from DataSource
        DataSource source = new DataSource(dataset);

        //get instance object
        Instances data = source.getDataSet();

        //building an FPGrowth model
        FPGrowth fpgrowth_model = new FPGrowth();
        fpgrowth_model.setNumRulesToFind(number_of_rules);
        fpgrowth_model.setLowerBoundMinSupport(sup_min);
        fpgrowth_model.setMinMetric(0);
        fpgrowth_model.buildAssociations(data);
        AssociationRules ARS = fpgrowth_model.getAssociationRules();
        List<AssociationRule> ruleList = ARS.getRules();

        //creating an arrayList to store frequentPatterns
        ArrayList<Collection<BinaryItem>> FP = new ArrayList<Collection<BinaryItem>>();

        //creating an arrayList to store total supports
        ArrayList<Double> total_support = new ArrayList<>();

        for (int i = 0; i < ruleList.size(); i++) {

            AssociationRule AR = ruleList.get(i);

            Collection premise = AR.getPremise();
            int premiseSupport = AR.getPremiseSupport();

            Collection consequence = AR.getConsequence();
            int consequenceSupport = AR.getConsequenceSupport();

            int totalSupport = AR.getTotalSupport();
            Collection<BinaryItem> baseFrequentPattern = new HashSet<BinaryItem>();

            Iterator iterator = premise.iterator();
            while (iterator.hasNext()) {
                baseFrequentPattern.add((BinaryItem) iterator.next());
            }

            iterator = consequence.iterator();
            while (iterator.hasNext()) {
                baseFrequentPattern.add((BinaryItem) iterator.next());
            }

            if (!FP.contains(baseFrequentPattern)) {
                FP.add(baseFrequentPattern);
                total_support.add((double) totalSupport);
            }

        }
        for (int i = 0; i < total_support.size(); i++) {
            total_support.set(i, (total_support.get(i) / data.size()));
        }

        System.out.println(FP.size());
        for (int i = 0; i < FP.size(); i++) {
            Collection<BinaryItem> base_FP = FP.get(i);
            boolean closed = true;
            for (int j = 0; j < FP.size(); j++) {

                if (FP.get(j).equals(base_FP)) {
                    continue;
                } else {
                    if (test(base_FP, FP.get(j))) {
                        if (total_support.get(i) <= total_support.get(j)) {
                            closed = false;
                            break;
                        }
                    }
                }

            }

            if (closed) {
                closed_pattern.add(base_FP);
            }

        }
        File_W File_W = new File_W("closed_patterns.txt");
        for (int i = 0; i < closed_pattern.size(); i++) {
            File_W.write_to_file(closed_pattern.get(i).toString() + "\n");
        }
        File_W.close_file();

        for (int i = 0; i < FP.size(); i++) {
            Collection<BinaryItem> base_FP = FP.get(i);
            boolean max = true;
            for (int j = 0; j < FP.size(); j++) {

                if (FP.get(j).equals(base_FP)) {

                    continue;
                } else {
                    if (test(base_FP, FP.get(j))) {
                        if (total_support.get(j) >= sup_min) {
                            max = false;
                            break;
                        }

                    }
                }
            }
            if (max) {
                Max_pattern.add(base_FP);
            }

        }
        File_W File_W2 = new File_W("max_patterns.txt");
        for (int i = 0; i < Max_pattern.size(); i++) {
            File_W2.write_to_file(Max_pattern.get(i).toString() + "\n");
        }
        File_W2.close_file();
    }

    public static boolean test(Collection<BinaryItem> base_FP, Collection<BinaryItem> super_sets) {
        boolean result = true;
        for (BinaryItem b : base_FP) {
            if (!super_sets.contains(b)) return false;
        }
        return result;
    }
}