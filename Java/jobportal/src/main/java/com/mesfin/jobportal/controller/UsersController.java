package com.mesfin.jobportal.controller;

import java.util.*;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;

import com.mesfin.jobportal.entity.Users;
import com.mesfin.jobportal.entity.UsersType;
import com.mesfin.jobportal.services.UsersTypeService;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestParam;


@Controller
public class UsersController {

    private final UsersTypeService usersTypeService;

    @Autowired
    public UsersController(UsersTypeService usersTypeService) {
        this.usersTypeService = usersTypeService;
    }
    @GetMapping("/register")    
    public String register(Model model){
        List<UsersType> usersTypes = usersTypeService.getAll();
        model.addAttribute("getAllTypes", usersTypes);
        model.addAttribute("users", new Users());
        return "register";
    }
}
