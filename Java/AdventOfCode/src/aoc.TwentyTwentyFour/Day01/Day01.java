package aoc.TwentyTwentyFour.Day01;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.Scanner;

public class Day01 {
    public ArrayList<String> getInputLines(String filename) throws FileNotFoundException {
        Scanner scanner = new Scanner(filename);
        ArrayList<String> inputLines = new ArrayList<>();
        while (scanner.hasNextLine()) {
            String line = scanner.nextLine();
            if (!line.isEmpty()) {
                inputLines.add(line);
            }
        }
        return inputLines;
    }
}
