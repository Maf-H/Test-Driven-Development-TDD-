package tacos;

import lombok.Data;
import lombok.RequiredArgsConstructor;

@Data // sets getter, setter, equals and hashcode on run time.
@RequiredArgsConstructor
public class Ingredients {

    private final String id;
    private final String name;
    private final Type type;

    public static enum Type{
        WRAP, PROTEIN, VEGGIES, CHEESE, SAUCE
    }
}
