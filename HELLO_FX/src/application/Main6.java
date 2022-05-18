package application;

import java.util.Arrays;
import java.util.Random;

import javafx.application.Application;
import javafx.event.Event;
import javafx.event.EventHandler;
import javafx.fxml.FXMLLoader;
import javafx.stage.Stage;
import javafx.scene.Parent;
import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.scene.control.Label;

public class Main6 extends Application {
	Label lbl1;
	Label lbl2;
	Label lbl3;
	Label lbl4;
	Label lbl5;
	Label lbl6;
	
    @Override
    public void start(Stage primaryStage) {
        try {
            Parent root = FXMLLoader.load(getClass().getResource("main6.fxml"));
            Scene scene = new Scene(root,400,400);
            scene.getStylesheets().add(getClass().getResource("application.css").toExternalForm());
            Button btn = (Button) scene.lookup("#btn");
            lbl1 = (Label) scene.lookup("#lbl1");
            lbl2 = (Label) scene.lookup("#lbl2");
            lbl3 = (Label) scene.lookup("#lbl3");
            lbl4 = (Label) scene.lookup("#lbl4");
            lbl5 = (Label) scene.lookup("#lbl5");
            lbl6 = (Label) scene.lookup("#lbl6");
            
            btn.setOnMouseClicked(new EventHandler<Event>() {
				@Override
				public void handle(Event event) {
					myclick();					
				}           	
			});
            primaryStage.setTitle("AppMain");
            primaryStage.setScene(scene);
            primaryStage.show();
            
        } catch(Exception e) {
            e.printStackTrace();
        }
    }
    
    public void myclick() {
    	int lotto[] = new int[6];
    	
		for(int i = 0; i < 6; i++) {	
			lotto[i]= (int)(Math.random() * 45) + 1;
			
			for(int j = 0; j < i; j++) {
				if(lotto[i] == lotto[j]) {
					i--;
				}
			}		
		}
		
		lbl1.setText("" + lotto[0]);
		lbl2.setText("" + lotto[1]);
		lbl3.setText("" + lotto[2]);
		lbl4.setText("" + lotto[3]);
		lbl5.setText("" + lotto[4]);
		lbl6.setText("" + lotto[5]);
	}

	public static void main(String[] args) {
        launch(args);
    }
}

