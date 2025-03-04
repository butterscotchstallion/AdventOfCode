package aoc.TwentyTwentyFour.Day01;

import org.junit.jupiter.api.Test;

import java.io.FileNotFoundException;
import java.util.ArrayList;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertNotNull;

public class Day01Test {
    @Test
    public void testDay01() throws FileNotFoundException {
        Day01 day01 = new Day01();
        ArrayList<String> input = day01.getInputLines("./ZenOfPython.txt");
        assertNotNull(input);
        assertEquals(19, input.size());
    }
}