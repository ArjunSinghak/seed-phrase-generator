#include "checksum.hpp"
#include <cstring>

namespace seed {

uint8_t compute_checksum(const std::vector<uint8_t>& data) {
    uint8_t checksum = 0;
    for (size_t i = 0; i < data.size(); ++i) {
        checksum ^= data[i];
        for (int j = 0; j < 8; ++j) {
            if (checksum & 0x80) {
                checksum = (checksum << 1) ^ 0x07;
            } else {
                checksum <<= 1;
            }
        }
    }
    return checksum;
}

} // namespace seed