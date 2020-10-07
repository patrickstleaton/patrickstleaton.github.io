/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package Panels;

/**
 *
 * @author Patrick Leaton
 */
public class Question6 extends javax.swing.JFrame {

    private int temp;
    /**
     * Creates new form Question6
     */
    public Question6() {
        initComponents();
    }
    
    public Question6(int totalScore) {
        initComponents();
        temp = totalScore;
    }

    /**
     * This method is called from within the constructor to initialize the form.
     * WARNING: Do NOT modify this code. The content of this method is always
     * regenerated by the Form Editor.
     */
    @SuppressWarnings("unchecked")
    // <editor-fold defaultstate="collapsed" desc="Generated Code">//GEN-BEGIN:initComponents
    private void initComponents() {

        btnGroup6 = new javax.swing.ButtonGroup();
        jPanel1 = new javax.swing.JPanel();
        lblHeader = new java.awt.Label();
        btnRadio1 = new javax.swing.JRadioButton();
        btnRadio2 = new javax.swing.JRadioButton();
        btnRadio3 = new javax.swing.JRadioButton();
        btnRadio4 = new javax.swing.JRadioButton();

        setDefaultCloseOperation(javax.swing.WindowConstants.DISPOSE_ON_CLOSE);

        lblHeader.setFont(new java.awt.Font("DialogInput", 1, 24)); // NOI18N
        lblHeader.setText("Q6. What's your Zodiac Sign?");

        javax.swing.GroupLayout jPanel1Layout = new javax.swing.GroupLayout(jPanel1);
        jPanel1.setLayout(jPanel1Layout);
        jPanel1Layout.setHorizontalGroup(
            jPanel1Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(javax.swing.GroupLayout.Alignment.TRAILING, jPanel1Layout.createSequentialGroup()
                .addContainerGap(85, Short.MAX_VALUE)
                .addComponent(lblHeader, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)
                .addGap(69, 69, 69))
        );
        jPanel1Layout.setVerticalGroup(
            jPanel1Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(jPanel1Layout.createSequentialGroup()
                .addGap(40, 40, 40)
                .addComponent(lblHeader, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)
                .addContainerGap(40, Short.MAX_VALUE))
        );

        btnGroup6.add(btnRadio1);
        btnRadio1.setText("Aries, Leo, Scorpio, Taurus");
        btnRadio1.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                btnRadio1ActionPerformed(evt);
            }
        });

        btnGroup6.add(btnRadio2);
        btnRadio2.setText("Pisces, Aquarius, Cancer, Libra");
        btnRadio2.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                btnRadio2ActionPerformed(evt);
            }
        });

        btnGroup6.add(btnRadio3);
        btnRadio3.setText("Gemini, Sagittarius, Capricorn, Virgo");
        btnRadio3.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                btnRadio3ActionPerformed(evt);
            }
        });

        btnGroup6.add(btnRadio4);
        btnRadio4.setText("I was born on a leap day, so technically I'm not even real");
        btnRadio4.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                btnRadio4ActionPerformed(evt);
            }
        });

        javax.swing.GroupLayout layout = new javax.swing.GroupLayout(getContentPane());
        getContentPane().setLayout(layout);
        layout.setHorizontalGroup(
            layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addComponent(jPanel1, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE)
            .addGroup(layout.createSequentialGroup()
                .addGap(84, 84, 84)
                .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.TRAILING)
                    .addComponent(btnRadio1, javax.swing.GroupLayout.Alignment.LEADING)
                    .addComponent(btnRadio3, javax.swing.GroupLayout.Alignment.LEADING)
                    .addComponent(btnRadio4, javax.swing.GroupLayout.Alignment.LEADING)
                    .addComponent(btnRadio2, javax.swing.GroupLayout.Alignment.LEADING))
                .addContainerGap(javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE))
        );
        layout.setVerticalGroup(
            layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(layout.createSequentialGroup()
                .addComponent(jPanel1, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)
                .addGap(18, 18, 18)
                .addComponent(btnRadio1)
                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.UNRELATED)
                .addComponent(btnRadio2)
                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.UNRELATED)
                .addComponent(btnRadio3)
                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.UNRELATED)
                .addComponent(btnRadio4)
                .addGap(0, 114, Short.MAX_VALUE))
        );

        pack();
    }// </editor-fold>//GEN-END:initComponents

    private void btnRadio1ActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_btnRadio1ActionPerformed
        int totalScore = 4;
        int what = getTemp();
        int total = what + totalScore;
        Question7 q7 = new Question7(total);
        q7.setVisible(true);
        this.setVisible(false);
        this.dispose();
        // TODO add your handling code here:
    }//GEN-LAST:event_btnRadio1ActionPerformed

    private void btnRadio2ActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_btnRadio2ActionPerformed
        int totalScore = 3;
        int what = getTemp();
        int total = what + totalScore;
        Question7 q7 = new Question7(total);
        q7.setVisible(true);
        this.setVisible(false);
        this.dispose();
        // TODO add your handling code here:
    }//GEN-LAST:event_btnRadio2ActionPerformed

    private void btnRadio3ActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_btnRadio3ActionPerformed
        int totalScore = 2;
        int what = getTemp();
        int total = what + totalScore;
        Question7 q7 = new Question7(total);
        q7.setVisible(true);
        this.setVisible(false);
        this.dispose();
        // TODO add your handling code here:
    }//GEN-LAST:event_btnRadio3ActionPerformed

    private void btnRadio4ActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_btnRadio4ActionPerformed
        int totalScore = 1;
        int what = getTemp();
        int total = what + totalScore;
        Question7 q7 = new Question7(total);
        q7.setVisible(true);
        this.setVisible(false);
        this.dispose();
        // TODO add your handling code here:
    }//GEN-LAST:event_btnRadio4ActionPerformed

    /**
     * @param args the command line arguments
     */
    public static void main(String args[]) {
        /* Set the Nimbus look and feel */
        //<editor-fold defaultstate="collapsed" desc=" Look and feel setting code (optional) ">
        /* If Nimbus (introduced in Java SE 6) is not available, stay with the default look and feel.
         * For details see http://download.oracle.com/javase/tutorial/uiswing/lookandfeel/plaf.html 
         */
        try {
            for (javax.swing.UIManager.LookAndFeelInfo info : javax.swing.UIManager.getInstalledLookAndFeels()) {
                if ("Nimbus".equals(info.getName())) {
                    javax.swing.UIManager.setLookAndFeel(info.getClassName());
                    break;
                }
            }
        } catch (ClassNotFoundException ex) {
            java.util.logging.Logger.getLogger(Question6.class.getName()).log(java.util.logging.Level.SEVERE, null, ex);
        } catch (InstantiationException ex) {
            java.util.logging.Logger.getLogger(Question6.class.getName()).log(java.util.logging.Level.SEVERE, null, ex);
        } catch (IllegalAccessException ex) {
            java.util.logging.Logger.getLogger(Question6.class.getName()).log(java.util.logging.Level.SEVERE, null, ex);
        } catch (javax.swing.UnsupportedLookAndFeelException ex) {
            java.util.logging.Logger.getLogger(Question6.class.getName()).log(java.util.logging.Level.SEVERE, null, ex);
        }
        //</editor-fold>

        /* Create and display the form */
        java.awt.EventQueue.invokeLater(new Runnable() {
            public void run() {
                new Question6().setVisible(true);
            }
        });
    }

    // Variables declaration - do not modify//GEN-BEGIN:variables
    private javax.swing.ButtonGroup btnGroup6;
    private javax.swing.JRadioButton btnRadio1;
    private javax.swing.JRadioButton btnRadio2;
    private javax.swing.JRadioButton btnRadio3;
    private javax.swing.JRadioButton btnRadio4;
    private javax.swing.JPanel jPanel1;
    private java.awt.Label lblHeader;
    // End of variables declaration//GEN-END:variables

    /**
     * @return the temp
     */
    public int getTemp() {
        return temp;
    }

    /**
     * @param temp the temp to set
     */
    public void setTemp(int temp) {
        this.temp = temp;
    }
}