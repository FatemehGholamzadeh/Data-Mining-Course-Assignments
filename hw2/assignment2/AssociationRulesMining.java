import java.util.ArrayList;
import java.util.Collection;
import java.util.HashSet;
import java.util.Iterator;
import java.util.List;

import weka.associations.AssociationRule;
import weka.associations.AssociationRules;
import weka.associations.BinaryItem;
import weka.associations.FPGrowth;
import weka.core.Instances;
import weka.core.converters.ConverterUtils.DataSource;


public class AssociationRulesMining {
	
   public static void main(String args[])throws Exception{
	   
	double minSup = 0.1;
	int numRules = 10000000;   
	   
    String dataset = "C:\\Program Files\\Weka-3-8\\data\\supermarket.arff";
    DataSource source = new DataSource(dataset);
    //get instance object
    Instances data=source.getDataSet();
    
    FPGrowth fpgrowth_model=new FPGrowth();
    fpgrowth_model.setNumRulesToFind(numRules);
    fpgrowth_model.setLowerBoundMinSupport(minSup);
    fpgrowth_model.setMinMetric(0);
    fpgrowth_model.buildAssociations(data);
    AssociationRules ARS = fpgrowth_model.getAssociationRules();
    List<AssociationRule> ruleList = ARS.getRules();
    
    ArrayList<Collection<BinaryItem>> frequentPatterns = new ArrayList<Collection<BinaryItem>>();
    
    
    for(int i = 0; i < ruleList.size(); i++) {
    	
    	AssociationRule AR = ruleList.get(i);
    	
    	Collection premise = AR.getPremise();
    	int premiseSupport = AR.getPremiseSupport();
    	
    	Collection consequence = AR.getConsequence();
    	int consequenceSupport = AR.getConsequenceSupport();
    	
    	int totalSupport = AR.getTotalSupport();
    	Collection<BinaryItem> baseFrequentPattern = new HashSet<BinaryItem>();	
    	
    	Iterator iterator = premise.iterator();
    	while(iterator.hasNext()) {
    		baseFrequentPattern.add((BinaryItem)iterator.next());
    	}
    	
    	iterator = consequence.iterator();
    	while(iterator.hasNext()) {
    		baseFrequentPattern.add((BinaryItem)iterator.next());
    	}
    	
    	if(!frequentPatterns.contains(baseFrequentPattern))
    		frequentPatterns.add(baseFrequentPattern);
    	
    
    }

    
    
  } 
}
