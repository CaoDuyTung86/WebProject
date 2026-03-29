import re

path = "d:\\clone repo\\WebProject\\backend\\ticket-booking\\src\\main\\java\\com\\booking\\api\\service\\AuthService.java"
with open(path, "r", encoding="utf-8") as f:
    text = f.read()

target = r'''        var userDetails = new org.springframework.security.core.userdetails.User\(
                user.getEmail\(\),
                user.getPassword\(\) != null \? user.getPassword\(\) : "",
                Collections.singletonList\(new SimpleGrantedAuthority\(user.getRole\(\)\)\)\);
        String token = jwtService.generateToken\(userDetails\);'''

replacement = r'''        var userDetails = new org.springframework.security.core.userdetails.User(
                user.getEmail(),
                user.getPassword() != null ? user.getPassword() : "",
                Collections.singletonList(new SimpleGrantedAuthority(user.getRole())));
        
        java.util.Map<String, Object> extraClaims = new java.util.HashMap<>();
        extraClaims.put("role", user.getRole());
        String token = jwtService.generateToken(extraClaims, userDetails);'''

text = re.sub(target, replacement, text)

with open(path, "w", encoding="utf-8") as f:
    f.write(text)
