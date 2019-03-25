/*
 * Patrick Leaton
 * hogwartsstudentsSQL
 * 
 */
package control;
import Panels.Dashboard;
import java.sql.*;
import java.text.DateFormat;
import java.text.SimpleDateFormat;
import java.util.ArrayList;
import model.Student;
import model.HouseDetail;

/**
 * This class allows for a connection to the hogwartsstudents SQL database.
 *
 * @author Patrick Leaton
 */
public class hogwartsstudentsSQL {
    Connection con = null;

    /**
     * This allows for a connection to the driver.
     */
    public hogwartsstudentsSQL() {
        try {
            con = DriverManager.getConnection("jdbc:mysql://localhost:3306/hogwartsstudents", "sakilauser", "s@kil@");
        } catch (SQLException se) {
            se.printStackTrace();
        }
    }

    /**
     * This parameter allows for a search of all students by first name or last
     * name.
     *
     * @param student_id
     * @return
     */
    public Student getStudent(int student_id) {
        Student student = null;
        try {
            PreparedStatement getOneStudent = con.prepareStatement(
                    "select * from hogwartsstudents where student_id = ?");
            getOneStudent.setInt(1, student_id);
            ResultSet results = getOneStudent.executeQuery();
            if (results.next()) {
                student = new Student(
                        results.getInt("student_id"),
                        results.getString("first_name"),
                        results.getString("last_name"),
                        results.getString("house"),
                        results.getDate("date_enrolled"));
            }

        } catch (SQLException se) {
            se.printStackTrace();
        }
        return student;
    }

    //---------------------------------------------------------------------------------
    /**
     * This parameter makes an array list for the students, with a try catch
     * statement, while functioning the database for student information.
     *
     * @return
     */
    public ArrayList getStudents() {
        ArrayList<Student> students = new ArrayList();

        try {
            PreparedStatement getStudents = con.prepareStatement(
                    "select * from hogwartsstudents ");

            ResultSet results = getStudents.executeQuery();
            while (results.next()) {
                students.add(new Student(
                        results.getInt("student_id"),
                        results.getString("first_name"),
                        results.getString("last_name"),
                        results.getString("house"),
                        results.getDate("date_enrolled")
                ));
            }

        } catch (SQLException se) {
            se.printStackTrace();
        }
        return students;
    }

    //-------------------------------------------------------------------------------
    /**
     * This allows the user to search the database and return the students, with
     * a try catch statement implemented.
     *
     * @param searchStr
     * @return
     */
    public ArrayList getStudents(String searchStr) {
        ArrayList<Student> students = new ArrayList();

        try {
            PreparedStatement getStudents = con.prepareStatement(
                    "select * from hogwartsstudents where last_name like ? or first_name like ?");
            getStudents.setString(1, "%" + searchStr + "%");
            getStudents.setString(2, "%" + searchStr + "%");

            ResultSet results = getStudents.executeQuery();
            while (results.next()) {
                students.add(new Student(
                        results.getInt("student_id"),
                        results.getString("first_name"),
                        results.getString("last_name"),
                        results.getString("house"),
                        results.getDate("date_enrolled")
                ));
            }

        } catch (SQLException se) {
            se.printStackTrace();
        }
        return students;
    }
    //-------------------------------------------------------------------------------

    
    /**
     * This parameter pulls up the row of all the information on the house when
     * the house_name value is passed, with a try catch statement, while
     * functioning the database for student information.
     *
     * @param house_name
     * @return
     */
    public HouseDetail getHouseDetail(String house_name) {
       HouseDetail house = null;
        try {
            PreparedStatement getHouseDetail = con.prepareStatement(
                    "select * from housedetail where house_name = ?");
            getHouseDetail.setString(1, house_name);
            ResultSet results = getHouseDetail.executeQuery();
            while (results.next()) {
                house = new HouseDetail(
                        results.getString("house_name"),
                        results.getString("founder"),
                        results.getString("house_gem"),
                        results.getString("animal"),
                        results.getString("element"),
                        results.getString("ghost")
                );
            }

        } catch (SQLException se) {
            se.printStackTrace();
        }
        return house;
    }
    
    /**
     * This method will query the database and find all belonging to each house.
     * From there it will return the first name, last name, and student ID.
     * 
     * @param searchStr this parameter is will hold the house name.
     * @return
     */
    public ArrayList getHouse(String searchStr) {
        ArrayList<Student> students = new ArrayList();

        try {
            PreparedStatement getStudents = con.prepareStatement(
                    "select * from hogwartsstudents where house like ?");
            getStudents.setString(1, "%" + searchStr + "%");

            ResultSet results = getStudents.executeQuery();
            while (results.next()) {
                students.add(new Student(
                        results.getInt("student_id"),
                        results.getString("first_name"),
                        results.getString("last_name"),
                        results.getString("house")));
            }

        } catch (SQLException se) {
            se.printStackTrace();
        }
        return students;
    }

    /**
     * This method will receive a student object and make a query to the database in order to add the student.
     * 
     *
     * @param student This parameter enrolls a new student.
     */
    public void enrollStudent(Student student) {

        try {
            java.sql.Date now = new java.sql.Date(System.currentTimeMillis());

            PreparedStatement updateStudent = con.prepareStatement("INSERT INTO hogwartsstudents(first_name, last_name, house, date_enrolled) VALUES(?, ?, ?, ?);");

            updateStudent.setString(1, student.getFirst_name());
            updateStudent.setString(2, student.getLast_name());
            updateStudent.setString(3, student.getHouse());
            updateStudent.setDate(4,now);
            
            updateStudent.executeUpdate();

            PreparedStatement newStudent = con.prepareStatement("SELECT * FROM hogwartsstudents WHERE first_name = ? AND last_name = ? AND house = ? AND date_enrolled = ?");

            newStudent.setString(1, student.getFirst_name());
            newStudent.setString(2, student.getLast_name());
            newStudent.setString(3, student.getHouse());
            newStudent.setDate(4, now);

            ResultSet results = newStudent.executeQuery();
            results.next();
            student.setStudent_id(results.getInt("student_id"));

        } catch (SQLException ex) {
            ex.printStackTrace();
        }
    }
}
