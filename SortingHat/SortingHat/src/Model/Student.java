/*
 * Patrick Leaton
 * Student
 *
 */
package model;

import java.text.DateFormat;
import java.text.SimpleDateFormat;
import java.util.Date;

/**
 * This class is focused around the student field in the hogwartsstudents database, currently being worked on.
 *
 * @author Patrick Leaton
 */
public class Student {

    private int student_id;
    private String first_name;
    private String last_name;
    private String house;
    private Date date_enrolled;
    DateFormat df = new SimpleDateFormat("yyyy-MM-dd");

    /**
     * These parameters are the id of the student, along with the first and last
     * names with the house the student belongs to.
     *
     * 
     * @param first_name
     * @param last_name
     * @param house
     */
    public Student (String first_name, String last_name, String house) {
        
        this.first_name = first_name;
        this.last_name = last_name;
        this.house = house;
        this.date_enrolled = new java.util.Date();
    }
    public Student (int student_id, String first_name, String last_name, String house) {
        this.student_id = student_id;
        this.first_name = first_name;
        this.last_name = last_name;
        this.house = house;
    }

    /**
     * These parameters are the student's id first name, last name, house and the last
     * update of the information, as well as the house.
     *
     *
     * @param first_name
     * @param last_name
     * @param house
     * @param date_enrolled
     */
    public Student(String first_name, String last_name, String house, Date date_enrolled) {
        this(first_name, last_name, house);
        this.date_enrolled = date_enrolled;
    }
    public Student(int student_id, String first_name, String last_name, String house, Date date_enrolled) {
        this(student_id, first_name, last_name, house);
        this.date_enrolled = date_enrolled;
    }
    public Student() {
        this("", "", "", new Date());

    }

    public String toString() {
        return String.format("Student ID: %s, First Name: %s, Last Name: %s, House: %s Last Update: %s\n", getStudent_id(), getFirst_name(), getLast_name(), getHouse(), df.format(getDate_enrolled()));
    }

    /**
     * This is a return of the student's id.
     *
     * @return the student_id
     */
    public int getStudent_id() {
        return student_id;
    }

    /**
     * This parameter sets the student's id.
     *
     * @param student_id the student_id to set
     */
    public void setStudent_id(int student_id) {
        this.student_id = student_id;
    }

    /**
     * This parameter gets the student's first name.
     *
     * @return the first_name
     */
    public String getFirst_name() {
        return first_name;
    }

    /**
     * This parameter sets the student's first name.
     *
     * @param first_name the first_name to set
     */
    public void setFirst_name(String first_name) {
        this.first_name = first_name;
    }

    /**
     * This parameter gets the student's last name.
     *
     * @return the last_name
     */
    public String getLast_name() {
        return last_name;
    }
        public String getHouse() {
        return house;
    }

    /**
     * This parameter sets the student's last name.
     *
     * @param last_name the last_name to set
     */
    public void setLast_name(String last_name) {
        this.last_name = last_name;
    }
    
     public void setHouse(String house) {
        this.house = house;
    }


    /**
     * This parameter gets the last update of the information.
     *
     * @return the date_enrolled
     */
    public Date getDate_enrolled() {
        return date_enrolled;
    }

    /**
     * This parameter sets the last update of the information.
     *
     * @param date_enrolled the date_enrolled to set
     */
    public void setDate_enrolled(Date date_enrolled) {
        this.date_enrolled = date_enrolled;
    }

}
