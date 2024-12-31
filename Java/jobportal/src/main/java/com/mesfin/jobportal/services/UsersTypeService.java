package com.mesfin.jobportal.services;

import com.mesfin.jobportal.entity.UsersType;
import com.mesfin.jobportal.repository.UsersTypeRepository;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

@Service
public class UsersTypeService {

    private final UsersTypeRepository usersTypeRepository;

    @Autowired
    public UsersTypeService(UsersTypeRepository usersTypeRepository) {
        this.usersTypeRepository = usersTypeRepository;
    }

    public List<UsersType> getAll(){
        return usersTypeRepository.findAll();
    }
}
