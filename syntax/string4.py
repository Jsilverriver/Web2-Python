# positional formating
print(
    "Lorem ipsum {} dolor sit amet, consectetuer adipiscing elit. {} Aenean commodo ligula eget dolor. {} Aenean massa.".format(
        "eugnag", 12, "megumi"
    )
)

# Named placeholder
print(
    "Lorem ipsum {first} dolor sit amet, consectetuer adipiscing elit. {second:d} Aenean commodo ligula eget dolor. {first} Aenean massa.".format(
        first="eungang", second=12
    )
)
# d는 digit의 약자. 꼭 숫자만 들어가야함. 아니면 에러.
