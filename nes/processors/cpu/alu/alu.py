class Alu:
    @staticmethod
    def sum(a_input, b_input, carry_in):
        output = a_input + b_input + carry_in

        if output > 0xff:
            carry_out = 1
            output &= 0xff
        else:
            carry_out = 0

        if (not a_input & 0x80 and not b_input & 0x80 and output & 0x80) or \
           (a_input & 0x80 and b_input & 0x80 and not output & 0x80):
            overflow = 1
        else:
            overflow = 0

        return output, carry_out, overflow

    @staticmethod
    def bitwise_and(a_input, b_input):
        return a_input & b_input

    @staticmethod
    def bitwise_or(a_input, b_input):
        return a_input | b_input

    @staticmethod
    def bitwise_xor(a_input, b_input):
        return a_input ^ b_input

    @staticmethod
    def shift_right(a_input, carry_in):
        carry_out = a_input & 0x01

        output = a_input >> 1

        if carry_in:
            output |= 0x80

        return output, carry_out
