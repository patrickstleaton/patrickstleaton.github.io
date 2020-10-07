/*
 * Patrick Leaton
 * HouseDetail
 *
 */
package model;

import java.text.DateFormat;
import java.text.SimpleDateFormat;

/**
 * This is an instantiation class for the HouseDetail method in the Control
 * class.
 *
 * @author Patrick Leaton
 */
public class HouseDetail {

    private String house_name;
    private String founder;
    private String house_gem;
    private String animal;
    private String element;
    private String ghost;

    /**
     * These parameters are for the columns in the housedetail table;
     *
     * @param house_name
     * @param founder
     * @param house_gem
     * @param animal
     * @param element
     * @param ghost
     */
    public HouseDetail(String house_name, String founder, String house_gem, String animal, String element, String ghost) {
        this.house_name = house_name;
        this.founder = founder;
        this.house_gem = house_gem;
        this.animal = animal;
        this.element = element;
        this.ghost = ghost;

    }

    /**
     * This is all of the strings needed for the query.
     */
    public HouseDetail() {
        this("", "", "", "", "", "");

    }

    public String toString() {
        return String.format("House Name: %s, Founder: %s, House Gym: %s, Animal: %s, Element: %s, Ghost %s\n", getHouse_name(), getFounder(), getHouse_gem(), getAnimal(), getElement(), getGhost());
    }

    /**
     * This returns the name of the house from the table;
     *
     * @return the house_name
     */
    public String getHouse_name() {
        return house_name;
    }

    /**
     * This returns the founder from the table;
     *
     * @return the founder
     */
    public String getFounder() {
        return founder;
    }

    /**
     * This returns the house gem from the table;
     *
     * @return the house_gem
     */
    public String getHouse_gem() {
        return house_gem;
    }

    /**
     * This returns the house animal from the table;
     *
     * @return the animal
     */
    public String getAnimal() {
        return animal;
    }

    /**
     * This returns the house element from the table;
     *
     * @return the element
     */
    public String getElement() {
        return element;
    }

    /**
     * This returns the house ghost from the table;
     *
     * @return the ghost
     */
    public String getGhost() {
        return ghost;
    }

}
