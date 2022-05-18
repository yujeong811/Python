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
import javafx.scene.input.KeyCode;
import javafx.scene.input.KeyEvent;

public class Main9 extends Application {
	TextField tf1;
	TextField tf2;
	TextField tf3;
	
    @Override
    public void start(Stage primaryStage) {
        try {
            Parent root = FXMLLoader.load(getClass().getResource("main9.fxml"));
            Scene scene = new Scene(root,400,400);
            scene.getStylesheets().add(getClass().getResource("application.css").toExternalForm());
            Button btn = (Button) scene.lookup("#btn");
            tf1 = (TextField) scene.lookup("#tf_Mine");
            tf2 = (TextField) scene.lookup("#tf_Com");
            tf3 = (TextField) scene.lookup("#tf_Result");
            
            btn.setOnMouseClicked(new EventHandler<Event>() {
				@Override
				public void handle(Event event) {
					myclick();
				}            	
			});
            tf1.setOnKeyPressed(new EventHandler<KeyEvent>() {
            	@Override
				public void handle(KeyEvent event) {
					if(event.getCode() == KeyCode.ENTER) {
						myclick();
					}
					
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
    	int ran = (int)(Math.random() * 3) + 1;
    	
    	if(ran == 1) {
    		tf2.setText("가위");
    	} else if(ran == 2){
    		tf2.setText("바위");
    	} else {
    		tf2.setText("보");
    	}
    	
		if(tf1.getText().equals(tf2.getText())) {
			tf3.setText("비김");
		} else if(tf1.getText().equals("가위") && tf2.getText().equals("바위") ||
				  tf1.getText().equals("바위") && tf2.getText().equals("보") ||
				  tf1.getText().equals("보") && tf2.getText().equals("가위")){
			tf3.setText("짐");
		} else {
			tf3.setText("이김");
		}
	}

	public static void main(String[] args) {
        launch(args);
    }
}

