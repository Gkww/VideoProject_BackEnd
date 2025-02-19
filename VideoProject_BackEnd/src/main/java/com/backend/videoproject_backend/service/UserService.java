package com.backend.videoproject_backend.service;
import com.backend.videoproject_backend.dto.TbFeedbackEntity;
import com.backend.videoproject_backend.dto.TbPhysicalEntity;
import com.backend.videoproject_backend.dto.TbUserEntity;

import java.util.List;
import java.util.Optional;

/**
 * @author 展驰
 * @version 1.0
 * 2022/10/06
 */
public interface UserService {

    String addUser(TbUserEntity tbUserEntity);

    void deleteUser(Integer id);

    List<TbUserEntity> findAllUser();

    Optional<TbUserEntity> findUserById(Integer id);

    void updateUser(TbUserEntity tbUserEntity);

    Optional<TbUserEntity> findUserByName(String name);

    Optional<TbUserEntity> findUserByPhone(String phone);

    Optional<TbPhysicalEntity> findPhysicalByUserId(Integer id);

    void addPhysical(TbPhysicalEntity tbPhysicalEntity);

    void postFeedback(TbFeedbackEntity tbFeedbackEntity);

    String updateUser2(Integer id,Integer gender,String email);

    String deleteUser2(Integer id);
}
