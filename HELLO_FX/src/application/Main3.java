package application;

import javafx.application.Application;
import javafx.event.Event;
import javafx.event.EventHandler;
import javafx.fxml.FXMLLoader;
import javafx.stage.Stage;
import javafx.scene.Parent;
import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.scene.control.Label;
import javafx.scene.control.TextField;

public class Main3 extends Application {
	TextField tf1;
	TextField tf2;
	TextField tf3;
	
    @Override
    public void start(Stage primaryStage) {
        try {
            Parent root = FXMLLoader.load(getClass().getResource("main3.fxml"));
            Scene scene = new Scene(root,400,400);
            scene.getStylesheets().add(getClass().getResource("application.css").toExternalForm());
            Button btn = (Button) scene.lookup("#btn");
            tf1 = (TextField) scene.lookup("#tf1");
            tf2 = (TextField) scene.lookup("#tf2");
            tf3 = (TextField) scene.lookup("#tf3");
            
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
    	String a = tf1.getText();
		String b = tf2.getText();
		
		int num1 = Integer.parseInt(a);
		int num2 = Integer.parseInt(b);
		
		int sum = num1 + num2;
		
		tf3.setText("" + sum);				
	}

	public static void main(String[] args) {
        launch(args);
    }
}

