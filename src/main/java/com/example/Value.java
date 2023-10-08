package com.example;

import io.micronaut.serde.annotation.Serdeable;

import java.util.List;
import java.util.UUID;

@Serdeable
public record Value(
        String value
) {
}
