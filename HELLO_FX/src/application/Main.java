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

public class Main extends Application {

    @Override
    public void start(Stage primaryStage) {
        try {
            Parent root = FXMLLoader.load(getClass().getResource("Hello.fxml"));
            Scene scene = new Scene(root,400,400);
            scene.getStylesheets().add(getClass().getResource("application.css").toExternalForm());
            Button btn = (Button) scene.lookup("#btn");
            Label lbl = (Label) scene.lookup("#lbl");
            btn.setOnMouseClicked(new EventHandler<Event>() {
				@Override
				public void handle(Event event) {
					lbl.setText("Good Evening");					
				}            	
			});
//            System.out.println(lbl.getText());
            primaryStage.setTitle("AppMain");
            primaryStage.setScene(scene);
            primaryStage.show();
            
        } catch(Exception e) {
            e.printStackTrace();
        }
    }
    
    public static void main(String[] args) {
        launch(args);
    }
}

