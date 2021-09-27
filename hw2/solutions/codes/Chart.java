package ir.aut;

import org.jfree.chart.ChartFactory;
import org.jfree.chart.ChartPanel;
import org.jfree.chart.JFreeChart;
import org.jfree.chart.plot.CategoryPlot;
import org.jfree.chart.plot.PlotOrientation;
import org.jfree.chart.renderer.category.BarRenderer;
import org.jfree.data.category.CategoryDataset;
import org.jfree.data.category.DefaultCategoryDataset;

import javax.swing.*;
import java.awt.*;
import java.util.ArrayList;

public class Chart extends JFrame {

    private static final long serialVersionUID = 1L;

    public Chart(String appTitle, ArrayList<Long> times2, ArrayList<Long> times, double[] minSup) {
        super(appTitle);

        // Create Dataset
        CategoryDataset dataset = createDataset(minSup, times, times2);

        //Create chart
        JFreeChart chart = ChartFactory.createBarChart(
                "Compare duration of Apriori and FP_Growth Algorithms", //Chart Title
                "Minimum Supports ", // Category axis
                "Time (ms)", // Value axis
                dataset,
                PlotOrientation.VERTICAL,
                true, true, false
        );
        /* Get instance of CategoryPlot */
        CategoryPlot plot = chart.getCategoryPlot();

        BarRenderer renderer = (BarRenderer) plot.getRenderer();

        renderer.setSeriesPaint(0, Color.ORANGE);
        renderer.setSeriesPaint(1, Color.MAGENTA);

        ChartPanel panel = new ChartPanel(chart);
        setContentPane(panel);
    }

    private CategoryDataset createDataset(double[] min_sup, ArrayList<Long> times, ArrayList<Long> times2) {
        DefaultCategoryDataset dataset = new DefaultCategoryDataset();


        for (int i = 0; i < times.size(); i++) {
            dataset.addValue(times2.get(i), "Apriori", String.valueOf(min_sup[i]));
            dataset.addValue(times.get(i), "FP_Growth", String.valueOf(min_sup[i]));

        }


        return dataset;
    }

}