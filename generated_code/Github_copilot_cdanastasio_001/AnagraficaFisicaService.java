package com.example.service;

import com.example.dto.AnagraficaFisicaDTO;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.stereotype.Service;
import org.springframework.web.client.RestTemplate;
import org.springframework.web.util.UriComponentsBuilder;

@Service
public class AnagraficaFisicaService {

    @Value("${arca.api.baseurl}")
    private String arcaBaseUrl;

    private final RestTemplate restTemplate;

    public AnagraficaFisicaService(RestTemplate restTemplate) {
        this.restTemplate = restTemplate;
    }

    public AnagraficaFisicaDTO getAnagraficaFisicaByCodiceFiscale(String codiceFiscale) {
        String url = UriComponentsBuilder
            .fromHttpUrl(arcaBaseUrl + "/api/anagrafica/fisica")
            .queryParam("codiceFiscale", codiceFiscale)
            .toUriString();

        return restTemplate.getForObject(url, AnagraficaFisicaDTO.class);
    }
}