from __future__ import division
from fer import FER
from PIL import Image
import csv
import os

#my_string = "106 121 122 124 139 138 134 134 139 141 153 152 156 163 166 167 167 169 148 120 124 124 120 118 120 116 110 106 111 114 112 108 101 107 112 117 115 116 113 108 114 121 130 142 148 152 150 154 111 120 114 139 157 130 129 134 137 140 147 152 156 164 170 173 175 174 168 158 147 132 130 132 127 122 120 115 111 118 125 127 127 120 112 120 111 117 133 134 136 139 133 131 127 130 133 136 106 107 109 156 150 120 129 129 135 144 145 145 156 162 169 170 174 169 173 177 178 165 156 156 153 158 150 143 142 137 147 152 150 149 145 151 158 161 156 154 144 134 127 135 132 130 142 138 111 97 116 163 132 120 127 132 135 138 139 148 156 159 166 169 170 169 171 174 179 178 180 181 177 178 174 173 170 162 167 167 163 168 171 176 173 175 178 176 169 159 144 121 123 142 151 152 111 90 132 167 124 124 121 131 138 142 142 146 159 160 164 170 169 168 170 168 170 173 177 179 180 171 172 172 176 174 170 174 178 172 175 172 174 174 173 177 177 177 162 143 118 132 145 151 100 88 147 163 121 119 126 132 131 135 148 154 161 162 162 166 168 167 166 168 172 171 168 175 177 173 172 173 177 176 171 169 176 180 177 175 177 174 173 179 177 180 176 165 139 120 126 146 94 88 152 149 117 111 121 126 135 133 137 148 147 155 162 164 159 156 164 171 174 174 173 174 177 178 174 174 176 173 176 178 179 178 175 170 176 175 175 178 178 181 177 172 160 135 122 129 90 108 168 134 111 108 124 125 130 137 141 144 146 151 160 162 162 161 165 165 167 171 171 170 170 176 176 170 173 170 176 179 177 179 178 175 181 176 178 180 180 182 171 170 174 148 122 123 81 109 172 130 103 112 120 121 133 144 140 145 149 145 152 154 154 165 159 163 165 165 166 169 173 172 176 167 174 173 176 176 170 178 183 175 173 174 173 174 178 181 186 168 171 140 124 126 87 116 163 130 113 116 112 120 128 141 139 139 145 143 146 150 152 163 161 165 165 166 169 172 176 176 172 171 178 173 173 178 176 174 175 176 172 164 174 178 173 175 177 170 152 139 138 127 90 130 162 121 104 104 109 117 127 131 127 127 139 143 143 142 153 155 151 158 165 163 164 165 169 171 166 168 174 171 174 177 176 174 175 173 165 173 175 171 171 172 178 176 169 164 135 130 92 129 152 118 106 101 105 113 119 120 123 129 132 132 137 143 142 151 151 152 154 154 164 153 152 159 166 163 166 170 169 168 170 171 167 167 167 174 170 174 175 171 178 178 168 164 149 144 96 128 148 122 114 108 107 104 106 105 108 118 125 128 139 136 140 144 144 143 146 154 154 159 150 147 157 159 151 149 147 147 135 127 120 117 135 150 160 168 166 170 173 178 173 170 155 130 92 122 157 122 106 94 72 58 52 60 68 72 84 91 107 119 125 125 129 142 142 145 147 142 147 147 145 142 138 133 131 120 99 96 92 80 76 72 85 115 143 163 170 172 174 172 147 130 89 119 160 125 95 65 51 61 70 84 92 97 102 78 80 99 101 103 125 130 135 146 146 135 144 155 149 141 140 130 129 123 112 119 118 122 119 109 90 75 83 126 165 165 165 160 147 141 89 116 151 122 89 93 109 119 122 122 118 107 87 76 78 78 80 86 102 120 129 127 138 143 142 146 141 136 127 126 123 132 119 128 133 144 148 144 148 140 132 128 139 159 161 156 144 146 78 104 143 123 113 123 137 128 119 94 86 80 74 68 69 66 75 79 75 106 121 122 135 137 132 133 137 127 118 123 101 100 102 118 121 123 128 146 155 155 166 170 156 161 164 155 152 153 67 104 144 124 115 102 87 87 92 92 74 72 80 68 64 58 71 75 73 88 112 121 132 128 137 144 140 120 98 88 99 90 89 87 96 87 101 122 140 154 159 165 168 167 170 170 159 144 75 100 137 123 107 85 69 63 56 55 56 30 31 45 45 48 45 69 77 79 96 115 132 144 146 154 145 114 79 86 98 93 71 59 45 39 59 95 103 113 147 163 173 172 172 175 153 146 84 99 139 112 86 73 53 104 127 56 113 81 24 57 51 87 59 57 68 81 103 133 150 159 162 153 140 121 118 74 132 150 71 133 84 25 51 59 81 101 109 145 149 156 165 171 167 150 96 95 140 108 66 47 66 159 164 94 99 47 50 105 87 155 99 61 69 86 113 143 161 163 164 154 150 146 110 84 167 157 86 111 60 50 93 80 103 100 103 112 127 148 168 170 170 162 112 109 135 109 71 75 82 127 146 133 122 118 133 141 148 138 104 81 91 95 113 142 169 169 168 169 158 148 135 112 118 136 117 103 106 126 148 146 165 142 126 134 145 164 172 173 176 173 116 106 145 124 124 127 100 85 93 101 108 116 127 143 130 128 113 110 109 111 120 144 169 175 167 161 161 160 155 135 110 93 101 119 129 128 133 127 133 124 137 162 163 155 156 171 178 171 112 97 144 148 147 156 148 140 129 118 122 125 130 141 140 147 122 127 122 119 120 145 174 174 168 153 159 164 160 152 154 147 129 120 123 122 130 145 154 161 158 167 167 169 164 164 175 174 112 101 145 143 142 150 148 149 152 148 148 149 150 154 155 142 127 130 121 113 125 143 169 174 168 158 160 158 150 147 156 168 171 166 164 172 172 173 173 165 164 169 169 169 166 169 167 160 104 104 152 141 144 145 142 143 140 144 152 150 159 158 156 137 130 125 121 111 121 149 158 166 161 156 154 154 148 138 141 154 152 159 157 153 164 160 157 160 155 160 164 171 169 175 168 160 94 110 173 145 138 141 143 142 142 142 139 143 150 152 144 124 121 114 115 116 119 146 159 162 160 148 151 148 141 129 139 140 139 139 145 147 147 150 146 154 142 144 147 153 167 172 164 161 70 92 169 141 127 141 143 135 139 141 143 146 144 142 133 126 110 109 118 124 129 149 159 165 158 149 151 144 131 113 131 138 137 139 134 141 142 151 144 141 143 141 137 146 151 159 167 165 93 123 164 132 127 127 140 134 139 140 148 144 139 139 130 125 114 110 122 140 140 156 167 173 165 159 160 143 123 114 119 133 130 140 137 142 154 155 139 139 140 138 139 139 145 154 162 160 93 120 156 116 121 121 127 124 137 144 162 155 146 134 125 112 106 109 139 159 127 119 146 152 161 163 165 146 116 99 106 115 114 126 138 151 161 160 151 139 141 134 135 142 142 143 155 154 96 120 156 115 118 119 127 129 133 154 168 162 140 129 113 107 104 114 117 126 99 87 88 109 125 112 119 141 124 97 90 102 105 113 124 138 169 168 156 137 134 129 135 134 136 141 146 139 98 118 161 118 116 118 118 125 126 140 149 148 121 109 106 94 109 119 98 113 64 66 87 93 91 56 84 126 156 140 86 83 99 100 113 124 142 156 143 131 133 132 129 126 133 138 139 138 96 102 169 114 111 115 118 118 125 126 122 117 107 100 94 90 113 124 115 108 110 104 110 107 111 138 148 153 156 163 116 66 87 100 106 116 119 127 127 132 132 127 126 128 126 135 142 139 103 87 156 113 103 109 111 107 113 114 106 98 101 103 92 96 124 128 120 123 134 136 138 126 145 166 162 162 156 157 138 76 80 98 111 106 111 113 123 125 126 125 122 120 117 126 135 128 109 85 144 132 99 104 104 98 96 100 97 97 98 96 86 97 131 133 140 145 142 150 158 155 162 162 146 148 162 160 168 110 76 88 107 102 99 112 108 122 113 114 116 114 121 130 127 111 107 94 120 142 105 94 91 103 98 100 93 96 96 96 78 98 133 118 91 71 79 83 97 116 107 92 86 85 107 121 143 120 75 79 92 93 98 105 107 117 116 112 110 115 124 128 124 92 105 102 87 144 104 76 81 95 90 93 95 98 100 98 74 65 64 56 58 71 94 90 91 88 101 110 118 116 116 103 58 43 57 72 89 99 101 111 113 110 105 104 116 120 123 117 112 100 104 107 82 122 124 92 94 98 87 78 91 99 103 108 73 51 42 62 126 166 187 188 186 176 202 210 201 207 197 151 57 54 97 94 95 104 105 111 100 82 93 115 123 118 123 119 86 163 107 104 102 99 139 115 100 103 107 96 82 105 117 111 96 109 102 71 83 128 152 162 178 165 149 147 136 127 103 84 102 143 149 135 111 109 108 112 97 100 126 133 134 134 133 103 119 231 106 104 109 92 125 141 106 105 112 116 112 125 125 124 128 136 132 121 94 62 67 78 85 83 82 89 90 88 85 118 152 153 152 155 139 119 122 118 121 132 132 138 138 129 123 95 204 233 106 104 105 106 98 148 130 115 110 124 137 131 125 132 135 135 141 148 144 108 81 82 100 102 118 125 120 106 128 158 158 166 166 157 158 140 135 136 139 141 133 139 134 130 105 184 227 222 105 107 110 90 93 115 148 130 115 127 129 123 140 135 143 148 154 154 155 158 129 120 111 110 108 119 120 141 160 162 169 174 164 163 161 157 148 152 154 159 153 144 135 116 177 232 220 220 113 95 76 136 225 183 126 149 126 110 119 126 138 148 151 158 153 155 147 146 139 129 118 109 104 116 148 157 160 151 159 166 162 164 164 161 155 155 158 155 148 125 121 181 220 224 225 219 70 100 188 236 231 205 132 107 142 132 117 112 125 151 145 149 146 145 155 142 134 131 127 122 131 136 146 152 162 162 160 166 162 162 160 152 160 153 153 132 119 133 178 215 206 211 219 220 154 227 236 209 156 100 112 94 81 142 153 122 118 134 140 142 143 134 149 151 147 141 153 160 158 154 161 165 166 160 164 163 159 162 159 148 152 144 137 120 144 190 201 200 201 201 208 208 238 219 181 129 105 108 118 121 104 80 115 149 144 127 126 124 127 140 140 148 155 154 153 164 169 170 164 160 167 163 162 166 163 154 156 151 145 113 101 163 201 198 203 195 201 202 201 198 193 150 105 106 115 124 125 130 131 123 92 78 103 129 132 117 121 121 130 138 147 155 152 149 165 172 164 162 165 164 165 167 158 149 143 124 97 107 168 197 190 200 206 207 199 203 192 202 121 101 107 114 118 126 129 133 122 124 127 112 52 51 75 120 130 111 116 120 131 149 144 143 155 163 168 170 160 157 165 158 148 139 104 74 110 180 194 188 190 194 197 204 204 202 195 200"

#my_string = None #paste mo dito yung list: for intance: "100 20 30 40..." walang bracket ah
pixel_list = [106, 111, 106, 111, 111, 100, 94, 90, 81, 87, 90, 92, 96, 92, 89, 89, 78, 67, 75, 84, 96, 112, 116, 112, 112, 104, 94, 70, 93, 93, 96, 98, 96, 103, 109, 107, 105, 104, 107, 106, 106, 105, 113, 70, 154, 238, 193, 121, 121, 120, 107, 97, 90, 88, 88, 108, 109, 116, 130, 129, 128, 122, 119, 116, 104, 104, 100, 99, 95, 109, 106, 97, 101, 104, 110, 92, 123, 120, 120, 118, 102, 87, 85, 94, 102, 107, 104, 104, 104, 107, 95, 100, 227, 219, 150, 101, 122, 114, 109, 116, 132, 147, 152, 168, 172, 163, 162, 152, 148, 157, 160, 151, 143, 144, 137, 139, 140, 135, 145, 144, 145, 152, 173, 169, 164, 156, 156, 161, 169, 156, 144, 120, 87, 82, 102, 109, 105, 110, 76, 188, 236, 181, 105, 107, 124, 139, 156, 163, 167, 163, 149, 134, 130, 130, 121, 118, 122, 122, 125, 122, 123, 124, 123, 112, 108, 109, 124, 148, 143, 141, 145, 141, 132, 116, 115, 118, 114, 113, 132, 142, 144, 122, 99, 92, 106, 90, 136, 236, 209, 129, 106, 114, 139, 157, 150, 132, 124, 121, 117, 111, 103, 113, 104, 106, 114, 106, 95, 89, 113, 115, 107, 86, 66, 71, 124, 147, 142, 144, 138, 127, 127, 121, 118, 116, 111, 103, 99, 105, 104, 124, 139, 125, 98, 93, 225, 231, 156, 105, 115, 118, 138, 130, 120, 120, 124, 119, 111, 108, 112, 116, 104, 101, 108, 94, 65, 93, 123, 102, 85, 73, 47, 75, 127, 156, 150, 145, 141, 141, 127, 121, 119, 118, 115, 109, 104, 94, 76, 92, 115, 141, 148, 115, 183, 205, 100, 108, 124, 126, 134, 129, 129, 127, 121, 126, 121, 124, 120, 112, 109, 105, 107, 72, 51, 109, 137, 87, 69, 53, 66, 82, 100, 148, 148, 142, 143, 143, 140, 127, 127, 118, 118, 111, 104, 91, 81, 94, 100, 106, 130, 148, 126, 132, 112, 118, 125, 129, 134, 134, 129, 132, 131, 132, 126, 125, 121, 120, 117, 113, 104, 58, 61, 119, 128, 87, 63, 104, 159, 127, 85, 140, 149, 143, 142, 135, 134, 124, 129, 125, 118, 107, 98, 103, 95, 98, 103, 105, 115, 130, 149, 107, 94, 121, 130, 133, 139, 137, 135, 135, 138, 131, 135, 130, 133, 128, 127, 119, 106, 52, 70, 122, 119, 92, 56, 127, 164, 146, 93, 129, 152, 140, 142, 139, 139, 137, 133, 126, 125, 113, 96, 98, 90, 87, 107, 112, 110, 115, 126, 142, 81, 104, 131, 122, 141, 140, 144, 138, 142, 135, 133, 137, 144, 141, 131, 120, 105, 60, 84, 122, 94, 92, 55, 56, 94, 133, 101, 118, 148, 144, 142, 141, 140, 144, 154, 140, 126, 114, 100, 100, 93, 78, 96, 116, 124, 127, 110, 132, 142, 80, 123, 124, 153, 147, 145, 139, 142, 148, 137, 141, 140, 139, 127, 123, 108, 68, 92, 118, 86, 74, 56, 113, 99, 122, 108, 122, 148, 152, 139, 143, 148, 162, 168, 149, 122, 106, 97, 93, 95, 91, 82, 112, 137, 129, 119, 117, 153, 115, 92, 127, 152, 152, 145, 148, 146, 154, 148, 144, 145, 139, 127, 129, 118, 72, 97, 107, 80, 72, 30, 81, 47, 118, 116, 125, 149, 150, 143, 146, 144, 155, 162, 148, 117, 98, 97, 96, 98, 99, 105, 125, 131, 123, 126, 112, 122, 149, 78, 112, 156, 156, 156, 156, 159, 161, 147, 146, 149, 145, 139, 132, 125, 84, 102, 87, 74, 80, 31, 24, 50, 133, 127, 130, 150, 159, 150, 144, 139, 146, 140, 121, 107, 101, 98, 96, 100, 103, 117, 125, 125, 140, 138, 125, 118, 144, 103, 52, 163, 164, 162, 159, 160, 162, 155, 151, 145, 143, 143, 132, 128, 91, 78, 76, 68, 68, 45, 57, 105, 141, 143, 141, 154, 158, 152, 142, 139, 134, 129, 109, 100, 103, 96, 96, 98, 108, 111, 124, 132, 135, 148, 151, 134, 127, 129, 51, 166, 170, 169, 166, 164, 162, 162, 160, 152, 146, 143, 137, 139, 107, 80, 78, 69, 64, 45, 51, 87, 148, 130, 140, 155, 156, 144, 133, 130, 125, 113, 106, 94, 92, 86, 78, 74, 73, 96, 128, 135, 143, 151, 145, 140, 126, 132, 75, 167, 173, 170, 169, 170, 166, 164, 162, 154, 150, 142, 143, 136, 119, 99, 78, 66, 58, 48, 87, 155, 138, 128, 147, 142, 137, 124, 126, 125, 112, 107, 94, 90, 96, 97, 98, 65, 51, 109, 136, 135, 148, 158, 149, 142, 124, 117, 120, 167, 175, 174, 170, 169, 168, 159, 162, 154, 152, 153, 142, 140, 125, 101, 80, 75, 71, 45, 59, 99, 104, 113, 122, 127, 130, 121, 110, 114, 106, 104, 109, 113, 124, 131, 133, 64, 42, 102, 132, 141, 154, 153, 146, 143, 127, 121, 130, 169, 174, 169, 169, 168, 167, 156, 161, 165, 163, 155, 151, 144, 125, 103, 86, 79, 75, 69, 57, 61, 81, 110, 127, 130, 125, 114, 109, 110, 109, 114, 119, 124, 128, 133, 118, 56, 62, 71, 121, 148, 154, 155, 145, 134, 140, 121, 111, 148, 168, 173, 171, 170, 166, 164, 165, 159, 161, 151, 151, 144, 129, 125, 102, 75, 73, 77, 68, 69, 91, 109, 122, 121, 121, 115, 118, 122, 139, 117, 98, 115, 120, 140, 91, 58, 126, 83, 94, 144, 155, 147, 155, 149, 140, 130, 116, 120, 158, 177, 174, 168, 168, 171, 165, 163, 165, 158, 152, 143, 142, 130, 120, 106, 88, 79, 81, 86, 95, 111, 119, 113, 111, 116, 124, 140, 159, 126, 113, 108, 123, 145, 71, 71, 166, 128, 62, 108, 158, 146, 142, 151, 148, 138, 120, 124, 147, 178, 179, 170, 172, 174, 167, 165, 165, 165, 154, 146, 142, 135, 129, 121, 112, 96, 103, 113, 113, 120, 120, 125, 121, 119, 129, 140, 127, 99, 64, 110, 134, 142, 79, 94, 187, 152, 67, 81, 129, 139, 134, 147, 155, 147, 131, 124, 132, 165, 178, 173, 171, 174, 171, 165, 166, 163, 154, 154, 145, 146, 127, 122, 121, 115, 133, 143, 142, 144, 145, 143, 149, 146, 149, 156, 119, 87, 66, 104, 136, 150, 83, 90, 188, 162, 78, 82, 120, 129, 131, 141, 154, 155, 149, 120, 130, 156, 180, 177, 168, 173, 171, 166, 169, 164, 164, 154, 147, 146, 138, 135, 132, 132, 150, 161, 169, 169, 174, 169, 158, 159, 159, 167, 146, 88, 87, 110, 138, 158, 97, 91, 186, 178, 85, 100, 111, 118, 127, 153, 153, 152, 144, 118, 132, 156, 181, 179, 175, 174, 170, 169, 172, 165, 153, 159, 142, 135, 143, 137, 128, 144, 159, 163, 169, 175, 174, 174, 166, 162, 165, 173, 152, 109, 93, 107, 126, 155, 116, 88, 176, 165, 83, 102, 110, 109, 122, 160, 164, 149, 143, 120, 127, 153, 177, 180, 177, 177, 170, 173, 176, 169, 152, 150, 147, 144, 142, 132, 137, 146, 162, 164, 168, 167, 168, 168, 161, 160, 158, 165, 161, 125, 91, 111, 145, 162, 107, 101, 202, 149, 82, 118, 108, 104, 131, 158, 169, 165, 155, 116, 122, 158, 178, 171, 173, 178, 176, 172, 176, 171, 159, 147, 147, 155, 146, 133, 144, 154, 153, 154, 169, 161, 153, 158, 156, 148, 149, 159, 163, 112, 56, 138, 166, 162, 92, 110, 210, 147, 89, 125, 119, 116, 136, 154, 170, 172, 163, 110, 120, 150, 174, 172, 172, 174, 176, 176, 172, 166, 166, 157, 145, 149, 141, 137, 140, 145, 140, 150, 158, 161, 159, 160, 154, 151, 151, 160, 165, 119, 84, 148, 162, 146, 86, 118, 201, 136, 90, 120, 120, 148, 146, 161, 164, 164, 168, 106, 115, 143, 173, 172, 173, 174, 170, 167, 171, 168, 163, 159, 142, 141, 136, 127, 120, 114, 121, 146, 148, 160, 164, 158, 154, 148, 144, 143, 146, 141, 126, 153, 162, 148, 85, 116, 207, 127, 88, 106, 141, 157, 152, 165, 160, 162, 170, 111, 111, 142, 170, 176, 177, 176, 173, 174, 178, 174, 166, 151, 138, 140, 127, 118, 98, 79, 118, 110, 135, 155, 160, 150, 148, 141, 131, 123, 116, 124, 156, 156, 156, 162, 107, 116, 197, 103, 85, 128, 160, 160, 162, 166, 167, 165, 160, 114, 118, 137, 162, 174, 176, 173, 170, 173, 173, 171, 170, 149, 133, 130, 126, 123, 88, 86, 74, 84, 112, 135, 152, 147, 138, 129, 113, 114, 99, 97, 140, 163, 157, 160, 121, 103, 151, 84, 118, 158, 162, 151, 162, 160, 163, 164, 157, 112, 125, 147, 167, 170, 171, 176, 176, 176, 173, 174, 169, 147, 131, 129, 123, 101, 99, 98, 132, 167, 118, 110, 154, 156, 141, 139, 131, 119, 106, 90, 86, 116, 138, 168, 143, 58, 57, 102, 152, 158, 169, 159, 160, 164, 162, 165, 165, 108, 127, 152, 167, 174, 169, 178, 179, 176, 178, 177, 168, 147, 120, 123, 132, 100, 90, 93, 150, 157, 136, 93, 147, 168, 154, 140, 138, 133, 115, 102, 83, 66, 76, 110, 120, 43, 54, 143, 153, 166, 174, 166, 166, 163, 166, 167, 158, 101, 127, 150, 163, 178, 176, 179, 177, 170, 176, 176, 170, 135, 99, 112, 119, 102, 89, 71, 71, 86, 117, 101, 129, 171, 152, 139, 137, 130, 114, 105, 99, 87, 80, 76, 75, 57, 97, 149, 152, 166, 164, 162, 162, 159, 163, 158, 148, 107, 120, 149, 168, 172, 180, 178, 179, 178, 174, 174, 171, 127, 96, 119, 128, 118, 87, 59, 133, 111, 103, 119, 120, 166, 159, 139, 139, 140, 126, 113, 100, 100, 98, 88, 79, 72, 94, 135, 155, 157, 163, 164, 162, 162, 154, 149, 139, 112, 112, 145, 171, 175, 177, 175, 178, 183, 175, 175, 167, 120, 92, 118, 133, 121, 96, 45, 84, 60, 106, 129, 123, 164, 157, 145, 134, 137, 138, 124, 113, 106, 111, 107, 92, 89, 95, 111, 139, 158, 161, 164, 160, 159, 156, 143, 104, 117, 120, 151, 176, 172, 175, 170, 175, 175, 176, 173, 167, 117, 80, 122, 144, 123, 87, 39, 25, 50, 126, 128, 122, 172, 153, 147, 141, 142, 151, 138, 124, 116, 106, 102, 93, 99, 104, 109, 119, 140, 157, 161, 152, 148, 151, 124, 74, 115, 111, 158, 173, 174, 177, 176, 181, 173, 172, 165, 167, 135, 76, 119, 148, 128, 101, 59, 51, 93, 148, 133, 130, 172, 164, 147, 142, 154, 161, 169, 142, 119, 111, 99, 98, 101, 105, 108, 122, 135, 148, 155, 160, 152, 145, 97, 110, 116, 117, 161, 175, 174, 174, 175, 176, 174, 164, 173, 174, 150, 72, 109, 144, 146, 122, 95, 59, 80, 146, 127, 145, 173, 160, 150, 151, 155, 160, 168, 156, 127, 113, 112, 105, 111, 111, 112, 118, 136, 152, 155, 153, 144, 113, 107, 180, 113, 133, 156, 178, 173, 173, 175, 178, 173, 174, 175, 170, 160, 85, 90, 148, 155, 140, 103, 81, 103, 165, 133, 154, 173, 157, 146, 144, 139, 151, 156, 143, 127, 123, 108, 107, 113, 100, 97, 121, 139, 154, 158, 153, 137, 101, 168, 194, 108, 134, 154, 176, 177, 179, 178, 180, 174, 178, 171, 174, 168, 115, 75, 140, 155, 154, 113, 101, 100, 142, 124, 161, 165, 160, 154, 141, 139, 139, 137, 131, 132, 125, 122, 117, 110, 82, 100, 132, 141, 159, 155, 132, 120, 163, 197, 188, 114, 136, 144, 169, 177, 177, 178, 180, 178, 173, 171, 175, 166, 143, 83, 132, 166, 159, 147, 109, 103, 126, 137, 158, 164, 155, 142, 143, 140, 141, 134, 133, 132, 126, 113, 116, 105, 93, 126, 132, 133, 153, 148, 119, 144, 201, 190, 190, 121, 139, 134, 159, 177, 180, 181, 182, 181, 175, 172, 171, 170, 163, 126, 128, 170, 165, 163, 145, 112, 134, 162, 167, 169, 160, 144, 141, 138, 134, 129, 132, 127, 125, 114, 112, 104, 115, 133, 138, 139, 144, 125, 133, 190, 198, 200, 194, 130, 133, 127, 144, 162, 176, 177, 171, 186, 177, 178, 178, 173, 170, 165, 139, 156, 168, 173, 149, 127, 145, 163, 167, 169, 164, 147, 137, 139, 135, 135, 129, 126, 122, 116, 110, 116, 123, 134, 138, 134, 135, 121, 178, 201, 203, 206, 197, 142, 131, 135, 121, 143, 165, 172, 170, 168, 170, 176, 178, 178, 172, 165, 159, 161, 167, 172, 156, 148, 164, 155, 169, 169, 171, 153, 146, 139, 142, 134, 126, 128, 120, 114, 115, 120, 118, 134, 129, 130, 116, 181, 215, 200, 195, 207, 204, 148, 127, 132, 123, 118, 139, 160, 174, 171, 152, 169, 168, 173, 174, 165, 161, 164, 170, 172, 165, 168, 172, 156, 164, 166, 169, 167, 151, 145, 142, 136, 133, 126, 117, 121, 124, 123, 123, 133, 123, 105, 177, 220, 206, 201, 201, 199, 204, 152, 130, 130, 142, 132, 120, 135, 148, 140, 139, 164, 164, 170, 172, 160, 156, 155, 170, 175, 171, 170, 173, 171, 164, 169, 175, 172, 159, 154, 143, 141, 138, 135, 126, 130, 128, 117, 119, 103, 95, 184, 232, 224, 211, 201, 202, 203, 202, 150, 133, 142, 151, 145, 126, 122, 122, 124, 138, 135, 149, 155, 147, 147, 144, 152, 159, 153, 167, 170, 176, 178, 175, 167, 168, 164, 167, 162, 155, 146, 139, 142, 135, 127, 124, 112, 86, 119, 204, 227, 220, 225, 219, 208, 201, 192, 195, 154, 136, 138, 152, 151, 146, 129, 123, 126, 127, 130, 144, 130, 130, 141, 146, 153, 144, 146, 150, 162, 173, 171, 174, 160, 160, 161, 165, 160, 154, 139, 138, 139, 128, 111, 92, 100, 163, 231, 233, 222, 220, 219, 220, 208, 198, 202, 200]#map(int,my_string.split())
#trying to check if the acquired pixel_list is the same as the original
new = Image.new(mode = "L", size = (48,48))
x = new.load()
k = 0
for i in range(48):
	for j in range(48):
		x[j,i] = pixel_list[k]
		k+=1
new.save("new.png")