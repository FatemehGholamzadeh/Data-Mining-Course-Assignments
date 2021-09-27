package ir.aut;

import weka.associations.Apriori;
import weka.associations.AssociationRule;
import weka.associations.AssociationRules;
import weka.associations.FPGrowth;
import weka.core.Instances;
import weka.core.converters.ConverterUtils.DataSource;

import javax.swing.*;
import java.util.ArrayList;
import java.util.List;

public class Question3 {
    public static void main(String args[]) throws Exception {

        //creating a double array for given min supports
        double[] sup_min = {0.05, 0.06, 0.07, 0.08, 0.09, 0.1, 0.11, 0.12, 0.13, 0.14, 0.15};

        //creating an arrayList to store duration of  PF_Growth  Algorithm
        ArrayList<Long> duration = new ArrayList<>();

        //creating an arrayList to store duration of  Apriori Algorithm
        ArrayList<Long> duration2 = new ArrayList<>();

        //address of the dataset file
        String dataset = "supermarket.arff";

        //creating an object from DataSource
        DataSource source = new DataSource(dataset);

        //getting an instance of DataSource
        Instances data = source.getDataSet();

        //implementation of apriori :

        for (int i = 0; i < sup_min.length; i++) {

            // getting the value of i_th element of sup_min array which shows minimum support for the duration
            String m_sup = String.valueOf(sup_min[i]);

            //setting options of algorithm
            String[] options = {"-N", "100000", "-C", "0.9", "-S", m_sup};

            //getting start time of apriori algorithm
            long t1 = System.currentTimeMillis();

            //building an apriori model
            Apriori apriori_model = new Apriori();
            apriori_model.setOptions(options);
            apriori_model.setMinMetric(0);
            apriori_model.buildAssociations(data);
            AssociationRules ARS2 = apriori_model.getAssociationRules();
            List<AssociationRule> ruleList2 = ARS2.getRules();

            //getting end time of apriori algorithm
            long t2 = System.currentTimeMillis();

            //calculating the duration of apriori algorithm
            System.out.println("duration of Apriori algorithm in " + i +"th round : "+ (t2 - t1));
            duration2.add(t2 - t1);
        }

        //implementation of FP_Growth :
        for (int i = 0; i < sup_min.length; i++) {

            // getting the value of i_th element of sup_min array which shows minimum support for the duration
            String m_sup = String.valueOf(sup_min[i]);

            //setting options of algorithm
            String[] options = {"-N", "100000", "-C", "0.9", "-S", m_sup};

            //getting start time of FP_Growth algorithm
            long start = System.currentTimeMillis();

            //building an FP_Growth model
            FPGrowth fpgrowth_model = new FPGrowth();
            fpgrowth_model.setOptions(options);
            fpgrowth_model.setMinMetric(0);
            fpgrowth_model.buildAssociations(data);
            AssociationRules ARS = fpgrowth_model.getAssociationRules();
            List<AssociationRule> ruleList = ARS.getRules();

            //getting end time of FP_Growth algorithm
            long end = System.currentTimeMillis();

            //calculating the duration of FP_Growth algorithm
            System.out.println("duration of FP_Growth algorithm in " + i +"th round : "+ (end - start));
            duration.add(end - start);

        }

        SwingUtilities.invokeAndWait(() -> {
            Chart example = new Chart("Bar Chart Window", duration2, duration, sup_min);
            example.setSize(1000, 800);
            example.setLocationRelativeTo(null);
            example.setDefaultCloseOperation(WindowConstants.EXIT_ON_CLOSE);
            example.setVisible(true);
        });

    }

}