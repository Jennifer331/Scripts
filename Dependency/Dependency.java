import com.opencsv.CSVReaderHeaderAware;
import com.opencsv.exceptions.CsvValidationException;

import java.io.IOException;
import java.io.FileReader;
import java.util.Map;

public class Dependency {
    public static void main(String[] args){
        System.out.println("Dependency Hello World! Hi!");
        try {
            Map<String, String> values = new CSVReaderHeaderAware(new FileReader("test.csv")).readMap();
        } catch(IOException|CsvValidationException e1) {
            System.err.println(e1);
        }
    }
}
