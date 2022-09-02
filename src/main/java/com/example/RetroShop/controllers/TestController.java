package com.example.RetroShop.controllers;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.annotation.Qualifier;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.ModelAttribute;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.servlet.ModelAndView;

import com.example.RetroShop.helper.ViewRouteHelper;

import java.nio.file.Files;

import javax.imageio.ImageIO;

import java.io.File;

@Controller
@RequestMapping("/")
public class TestController {

    @GetMapping("getimagen")
    public ModelAndView gefoto(){
        ModelAndView mav = new ModelAndView(ViewRouteHelper.FOTO);
        return mav;
    }






    
}
