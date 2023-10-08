package com.example;

import io.micronaut.http.annotation.Controller;
import io.micronaut.http.annotation.Get;
import io.micronaut.http.annotation.QueryValue;

import javax.sql.DataSource;
import java.sql.*;
import java.util.Optional;

@Controller
public class TestController {
    private final DataSource dataSource;

    public TestController(DataSource dataSource) {
        this.dataSource = dataSource;
    }

    @Get("/test")
    public Value test(@QueryValue("value") Optional<String> value) throws Exception {
        String selectResult = null;
        try (Connection connection = dataSource.getConnection()) {
            PreparedStatement preparedStatement = connection
                    .prepareStatement("SELECT uuid()");
            ResultSet resultSet = preparedStatement.executeQuery();
            while (resultSet.next()) {
                selectResult = resultSet.getString(1);
            }
        }
        return new Value(value.orElse("") + " " + selectResult);
    }
}
