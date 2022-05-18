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

public class Main4 extends Application {
	TextField tf1;
	TextField tf2;
	TextField tf3;
	
    @Override
    public void start(Stage primaryStage) {
        try {
            Parent root = FXMLLoader.load(getClass().getResource("main4.fxml"));
            Scene scene = new Scene(root,400,400);
            scene.getStylesheets().add(getClass().getResource("application.css").toExternalForm());
            Button btn = (Button) scene.lookup("#btn");
            tf1 = (TextField) scene.lookup("#tfMine");
            tf2 = (TextField) scene.lookup("#tfCom");
            tf3 = (TextField) scene.lookup("#tfResult");
            
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
    	int ran = (int)Math.random() * 2 + 1;
    	
    	if(ran == 1) {
    		tf2.setText("홀");
    	} else {
    		tf2.setText("짝");
    	} 
    	
		if(tf1.getText().equals(tf2.getText())) {
			tf3.setText("이김");
		} else {
			tf3.setText("짐");
		} 		
	}

	public static void main(String[] args) {
        launch(args);
    }
}

