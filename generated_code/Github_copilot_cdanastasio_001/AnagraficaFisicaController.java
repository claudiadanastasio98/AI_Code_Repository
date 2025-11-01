package com.example.controller;

import com.example.dto.AnagraficaFisicaDTO;
import com.example.service.AnagraficaFisicaService;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class AnagraficaFisicaController {
    private final AnagraficaFisicaService service;

    public AnagraficaFisicaController(AnagraficaFisicaService service) {
        this.service = service;
    }

    @GetMapping("/anagrafica/fisica")
    public AnagraficaFisicaDTO getByCodiceFiscale(@RequestParam String codiceFiscale) {
        return service.getAnagraficaFisicaByCodiceFiscale(codiceFiscale);
    }
}