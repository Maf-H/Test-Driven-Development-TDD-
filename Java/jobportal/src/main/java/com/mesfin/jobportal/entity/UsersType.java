package com.mesfin.jobportal.entity;

import java.util.List;

import jakarta.persistence.*;

@Entity
@Table(name = "users_type") // This annotation is used to specify the table name in the database
public class UsersType {

    @Id
    @GeneratedValue(strategy = GenerationType.AUTO) // This annotation is used to specify the primary key generation
                                                    // strategy
    private int userTypeId;
    private String userTypeName;
    @OneToMany(targetEntity = Users.class, mappedBy = "userTypeId", cascade = CascadeType.ALL)
    private List<Users> users;

    public UsersType() {
    }

    public UsersType(int userTypeId, String userTypeName, List<Users> users) {
        this.userTypeId = userTypeId;
        this.userTypeName = userTypeName;
        this.users = users;
    }

    public int getUserTypeId() {
        return userTypeId;
    }

    public void setUserTypeId(int userTypeId) {
        this.userTypeId = userTypeId;
    }

    public String getUserTypeName() {
        return userTypeName;
    }

    public void setUserTypeName(String userTypeName) {
        this.userTypeName = userTypeName;
    }

    public List<Users> getUsers() {
        return users;
    }

    public void setUsers(List<Users> users) {
        this.users = users;
    }

    @Override
    public String toString() {
        return "UsersType [userTypeId=" + userTypeId + ", userTypeName=" + userTypeName + ", users=" + users + "]";
    }
}
